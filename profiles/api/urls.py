from django.urls import path

from profiles.api.views import ProfileList

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),

]
