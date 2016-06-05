# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.gis.geos import fromstr
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from meeting.models import Meeting, User_attends_meeting


class TestMeetingCreationAPI(TestCase):
    urls = 'meeting.api_urls'

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

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }

        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_authenticated(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }

        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_is_superuser(self):
        user = self.create_superuser(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }

        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_only_meeting_to_future(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time - datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }

        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_owner_is_user(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }

        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meeting.objects.all()[0].creator.id, user.id)
        self.assertEqual(Meeting.objects.all().count(), 1)


class TestMeetingDeletionAPI(TestCase):
    urls = 'meeting.api_urls'

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

    def test_OK(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }
        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        meeting = Meeting.objects.all()[0]

        response = client.delete("/meetings/" + str(meeting.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_superuser(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }
        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        meeting = Meeting.objects.all()[0]

        user = self.create_superuser(username='username2', password='password2')
        client = APIClient()
        client.login(username='username2', password='password2')
        response = client.delete("/meetings/" + str(meeting.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_forbidden_others_creator(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=5)
        data = {
            "title": "HOLA",
            "position": "POINT(40.383333 -3.716667)",
            "time": time.strftime("%Y-%m-%dT%H:%M")
        }
        response = client.post("/meetings/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        meeting = Meeting.objects.all()[0]

        user = self.create_user(username='username2', password='password2')
        client = APIClient()
        client.login(username='username2', password='password2')
        response = client.delete("/meetings/" + str(meeting.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestGeoSearchMeetingAPI(TestCase):
    urls = 'meeting.api_urls'

    def setUp(self):
        self.random_user = self.create_user('random', 'random12345')

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

    def test_OK(self):
        time = datetime.datetime.now() + datetime.timedelta(days=5)

        pnt = fromstr('POINT(3.5 -1.2)', srid=4326)
        Meeting.objects.create(time=time, creator=self.random_user, position=pnt, title='meeting 1')

        self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/meetings/?distance=2000&lat=3.5&lon=-1.2", format='json')
        self.assertEquals(len(response.data.get('features')), 1)
        response = client.get("/meetings/?distance=2000&lat=3.517&lon=-1.2", format='json')
        self.assertEquals(len(response.data.get('features')), 1)
        response = client.get("/meetings/?distance=2000&lat=3.52&lon=-1.2", format='json')
        self.assertEquals(len(response.data.get('features')), 0)

        Meeting.objects.create(time=time, creator=self.random_user, position=pnt, title='meeting 2')
        response = client.get("/meetings/?distance=2000&lat=3.5&lon=-1.2", format='json')
        self.assertEquals(len(response.data.get('features')), 2)

    def test_only_future_meetings(self):
        time = datetime.datetime.now() + datetime.timedelta(days=5)

        pnt = fromstr('POINT(3.5 -1.2)', srid=4326)
        Meeting.objects.create(time=time, creator=self.random_user, position=pnt, title='meeting 1')
        Meeting.objects.create(time=time - datetime.timedelta(days=7), creator=self.random_user, position=pnt,
                               title='meeting 2')

        self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/meetings/?distance=2000&lat=3.5&lon=-1.2", format='json')
        self.assertEquals(len(response.data.get('features')), 1)

# Attend meeting:


class TestAttendMeetingCreationAPI(TestCase):
    urls = 'meeting.api_urls'

    def setUp(self):
        self.random_user = self.create_user('random', 'random12345')
        time = datetime.datetime.now() + datetime.timedelta(days=5)
        pnt = fromstr('POINT(3.5 -1.2)', srid=4326)
        self.meeting = Meeting.objects.create(time=time, creator=self.random_user, position=pnt, title='meeting 1')

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
            "meeting": self.meeting.id,
            "user": user.id
        }

        response = client.post("/attendances/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_authenticated(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        data = {
            "meeting": str(self.meeting.id),
            "user": user.id
        }

        response = client.post("/attendances/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_only_one_attendance(self):
        user = self.create_user(username='username', password='password')
        client = APIClient()
        client.login(username='username', password='password')

        data = {
            "meeting": str(self.meeting.id),
            "user": user.id
        }

        response = client.post("/attendances/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.post("/attendances/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestAttendMeetingListAPI(TestCase):
    urls = 'meeting.api_urls'

    def setUp(self):
        self.random_user = self.create_user('random', 'random12345')
        time = datetime.datetime.now() + datetime.timedelta(days=5)
        pnt = fromstr('POINT(3.5 -1.2)', srid=4326)
        self.meeting = Meeting.objects.create(time=time, creator=self.random_user, position=pnt, title='meeting 1')

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

        response = client.get("/attendances/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_authenticated(self):
        user = self.create_user(username='username', password='password')
        User_attends_meeting.objects.create(user=user, meeting=self.meeting)
        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/attendances/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_only_owned(self):
        user = self.create_user(username='username', password='password')
        User_attends_meeting.objects.create(user=user, meeting=self.meeting)
        User_attends_meeting.objects.create(user=self.random_user, meeting=self.meeting)
        client = APIClient()
        client.login(username='username', password='password')

        response = client.get("/attendances/", format='json')
        self.assertEqual(len(response.data), 1)


class TestAttendMeetingDeletionAPI(TestCase):
    urls = 'meeting.api_urls'

    def setUp(self):
        self.random_user = self.create_user('random', 'random12345')
        time = datetime.datetime.now() + datetime.timedelta(days=5)
        pnt = fromstr('POINT(3.5 -1.2)', srid=4326)
        self.meeting = Meeting.objects.create(time=time, creator=self.random_user, position=pnt, title='meeting 1')

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
        attendance = User_attends_meeting.objects.create(user=user, meeting=self.meeting)

        response = client.delete("/attendances/" + str(attendance.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_authenticated(self):
        user = self.create_user(username='username', password='password')
        attendance = User_attends_meeting.objects.create(user=user, meeting=self.meeting)

        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/attendances/" + str(attendance.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_only_owned(self):
        user = self.create_user(username='username', password='password')
        attendance = User_attends_meeting.objects.create(user=self.random_user, meeting=self.meeting)
        client = APIClient()
        client.login(username='username', password='password')

        response = client.delete("/attendances/" + str(attendance.id) + "/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
