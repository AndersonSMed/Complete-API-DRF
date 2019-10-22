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

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(users.count(), 1)

    def test_list_user(self):

        response = self.client.get(reverse('user-list'))
        users = UserSerializer(User.objects.all(), many = True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, users.data)

    def test_detail_user(self):
        
        data = {
            "username": "test",
            "email": "test@test.com",
            "password": "123456"
        }

        user = User.objects.create(**data)
        serializer = UserSerializer(user, many = False)
        response = self.client.get(reverse('user-detail', args=[user.pk]))
        
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_user(self):

        data = {
            "username": "test",
            "email": "test@test.com",
            "password": "123456"
        }

        new_data = {
            "username": "test123",
            "email": "test123@test.com"
        }

        user = User.objects.create(**data)
        response = self.client.patch(reverse('user-detail', args=[user.pk]), data = new_data)

        self.assertEqual(response.data.get('username'), new_data.get('username'))
        self.assertEqual(response.data.get('email'), new_data.get('email'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)