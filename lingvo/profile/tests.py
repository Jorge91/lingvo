# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from profile.models import Profile


class TestCustomUserRetrieveAPI(TestCase):
    urls = 'profile.api_urls'

    def create_user(self, username, password):
        user = User()
        user.username = username
        user.password = make_password(password)
        user.email = username + '@lingvo.com'
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.save()
        return user


    def test_user_not_authenticated(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        response = client.get("/profiles/{0}/".format(user.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_has_permission(self):
        user = self.create_user(username='username', password='password')

        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/profiles/{0}/".format(user.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_user_is_superuser(self):
        user = self.create_superuser(username='username', password='password')

        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/profiles/{0}/".format(user.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_user_is_superuser_not_found(self):
        self.create_superuser(username='username', password='password')

        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/profiles/0/", format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        client.logout()


class TestCustomUserUpdateAPI(TestCase):
    urls = 'profile.api_urls'

    def create_user(self, username, password):
        user = User()
        user.username = username
        user.password = make_password(password)
        user.email = username + '@lingvo.com'
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.save()
        return user


    def test_user_not_authenticated(self):
        user = self.create_user(username='username', password='password')
        profile = Profile.objects.get(user=user)
        client = APIClient()

        data = {
            "description": "desc",
            "genre": "MSC"
        }

        response = client.patch("/profiles/{0}/".format(profile.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_superuser(self):
        user = self.create_superuser(username='username', password='password')
        profile = Profile.objects.get(user=user)

        client = APIClient()
        client.login(username='username', password='password')

        data = {
            "description": "desc",
            "genre": "MSC"
        }

        response = client.patch("/profiles/{0}/".format(profile.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_user_is_superuser_request_user_not_login(self):
        user = self.create_superuser(username='prueba', password='prueba')
        profile = Profile.objects.get(user=user)

        client = APIClient()
        client.login(username='username', password='password')

        data = {
            "description": "desc",
            "genre": "MSC"
        }

        response = client.patch("/profiles/{0}/".format(profile.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        client.logout()

    def test_user_is_superuser_not_found(self):
        user = self.create_superuser(username='username', password='password')
        profile = Profile.objects.get(user=user)

        client = APIClient()
        client.login(username='username', password='password')

        data = {
            "description": "desc",
            "genre": "MSC"
        }

        response = client.patch("/profiles/0/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        client.logout()

    def test_ok(self):
        user = self.create_user(username='username', password='password')
        profile = Profile.objects.get(user=user)
        client = APIClient()
        client.login(username='username', password='password')

        data = {
            "description": "desc",
            "genre": "MSC"
        }

        response = client.patch("/profiles/{0}/".format(profile.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertNotEqual(Profile.objects.get(user=user).description, profile.description)

        client.logout()