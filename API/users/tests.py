from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from .serializer import UserSerializer

class UsersTests(APITestCase):

    def test_create_user(self):
        
        data = {
            "username": "anderson.med",
            "email": "anderson.santos.medeiros@hotmail.com",
            "password": "123456"
        }

        response = self.client.post(reverse('user-list'), data=data)
        users = User.objects.filter(**data)
        serializer = UserSerializer(users.last(), many = False)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(users.count(), 1)

    def test_list_user(self):

        response = self.client.get(reverse('user-list'))
        users = UserSerializer(User.objects.all(), many = True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, users.data)