from rest_framework.fields import SerializerMethodField, SlugField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from questions.models import Answer, Question


class AnswerSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)
    created_at = SerializerMethodField(read_only=True)
    likes_count = SerializerMethodField(read_only=True)
    user_has_voted = SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        exclude = ['question', 'voters', 'updated_at']

    def get_created_at(self, insatnce):
        return insatnce.created_at.strftime('%d &B &Y')

    def get_likes_count(self, insatnce):
        return insatnce.voters.count()

    def get_user_has_voted(self, insatnce):
        request = self.context.get('request')
        return insatnce.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)
    created_at = SerializerMethodField(read_only=True)
    slug = SlugField(read_only=True)
    answer_count = SerializerMethodField(read_only=True)
    user_has_answered = SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ['updated_at']

    def get_created_at(self, insatnce):
        return insatnce.created_at.strftime('%d &B &Y')

    def get_answer_count(self, insatnce):
        return insatnce.answers.count()

    def get_user_has_answered(self, insatnce):
        request = self.context.get('request')
        return insatnce.answers.filter(pk=request.user.pk).exists()
