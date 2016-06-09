# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from language.models import Language, User_practices_language, User_speaks_language


class TestAddSpeakLanguageAPI(TestCase):
    urls = 'language.api_urls'

    def setUp(self):
        self.language_es = Language.objects.create(code='ES', name='spanish')

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
        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        response = client.post("/languages/speak/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_authenticated(self):
        user = self.create_user(username='username', password='password')
        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        client = APIClient()
        client.login(username='username', password='password')

        response = client.post("/languages/speak/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_user_is_superuser(self):
        user = self.create_superuser(username='username', password='password')

        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        client = APIClient()
        client.login(username='username', password='password')

        response = client.post("/languages/speak/", data, format='json')
        print response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_language_already_added(self):
        user = self.create_user(username='username', password='password')
        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        client = APIClient()
        client.login(username='username', password='password')

        response = client.post("/languages/speak/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.post("/languages/speak/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        client.logout()


class TestDeleteSpeakLanguageAPI(TestCase):
    urls = 'language.api_urls'

    def setUp(self):
        self.language_es = Language.objects.create(code='ES', name='spanish')
        self.user = self.create_user(username='username', password='password')
        self.practice = User_speaks_language.objects.create(user=self.user, language=self.language_es)

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
        client = APIClient()

        response = client.delete("/languages/speak/" + str(self.practice.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_authenticated(self):
        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/languages/speak/" + str(self.practice.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        client.logout()

    def test_user_is_superuser(self):
        self.user.is_superuser = True
        self.user.save()

        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/languages/speak/" + str(self.practice.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        client.logout()

    def test_delete_other_users(self):
        new_user = self.create_user(username='username2', password='password')
        new_practice = User_speaks_language.objects.create(user=new_user, language=self.language_es)


        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/languages/speak/" + str(new_practice.id) + "/", format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        client.logout()




class TestAddPracticesLanguageAPI(TestCase):
    urls = 'language.api_urls'

    def setUp(self):
        self.language_es = Language.objects.create(code='ES', name='spanish')

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
        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        response = client.post("/languages/practice/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_authenticated(self):
        user = self.create_user(username='username', password='password')
        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        client = APIClient()
        client.login(username='username', password='password')

        response = client.post("/languages/practice/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_user_is_superuser(self):
        user = self.create_superuser(username='username', password='password')

        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        client = APIClient()
        client.login(username='username', password='password')

        response = client.post("/languages/practice/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_language_already_added(self):
        user = self.create_user(username='username', password='password')
        data = {
            "user": user.id,
            "language": self.language_es.id
        }

        client = APIClient()
        client.login(username='username', password='password')

        response = client.post("/languages/practice/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.post("/languages/practice/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        client.logout()


class TestDeletePracticesLanguageAPI(TestCase):
    urls = 'language.api_urls'

    def setUp(self):
        self.language_es = Language.objects.create(code='ES', name='spanish')
        self.user = self.create_user(username='username', password='password')
        self.practice = User_practices_language.objects.create(user=self.user, language=self.language_es)

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
        client = APIClient()

        response = client.delete("/languages/practice/" + str(self.practice.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_authenticated(self):
        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/languages/practice/" + str(self.practice.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        client.logout()

    def test_user_is_superuser(self):
        self.user.is_superuser = True
        self.user.save()

        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/languages/practice/" + str(self.practice.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        client.logout()

    def test_delete_other_users(self):
        new_user = self.create_user(username='username2', password='password')
        new_practice = User_practices_language.objects.create(user=new_user, language=self.language_es)


        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/languages/practice/" + str(new_practice.id) + "/", format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        client.logout()



