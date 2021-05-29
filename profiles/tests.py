import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase


# Create your tests here.


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'testcase', 'email': 'test@gnail.co.za', 'password1': 'str0ngpass',
                'password2': 'str0ngpass'}
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):
    list_url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create_user(username='davinci', password='str0ngpass!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_profile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, 'davinci')

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse('profile-detail', kwargs={'pk': 1}),
                                   {'city': 'Anchiano', 'bio': 'Big Man UNO'})
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {'id': 1, 'user': 'davinci', 'city': 'Anchiano', 'bio': 'Big Man UNO', 'avatar': None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username='random', password='lastp@ss')
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse('profile-detail', kwargs={'pk': 1}),
                                   {'city': 'Anchiano', 'bio': 'Hacked'})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
