from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .models import Todo, Project
from users.models import MyUsers


class TestWork(TestCase):
    def test_todo_all(self):
        user_admin = MyUsers.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        client = APIClient()
        client.force_authenticate(user=user_admin)
        response = client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_todo(self):
        user_admin = MyUsers.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        # print(user)
        client = APIClient()
        client.force_authenticate(user=user_admin)
        project = Project.objects.create(name='https://vk.com/im?sel=218588853')
        user = MyUsers.objects.create(username='Step', email='Step@gmail.com')
        project.users.add(user)
        project.save()
        todo = Todo.objects.create(project=project, text='1231', user=user)
        response = client.get(f'/api/todo/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todo(self):
        user_admin = MyUsers.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        # print(user)
        client = APIClient()
        client.force_authenticate(user=user_admin)
        project = Project.objects.create(name='https://vk.com/im?sel=218588853')
        user = MyUsers.objects.create(username='Step', email='Step@gmail.com')
        project.users.add(user)
        project.save()
        # todo = Todo.objects.create(project=project, text='1231', user=user)
        response = client.post(f'/api/todo/', {'project': project.id, 'text': '123123', 'user': user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_project_all(self):
        user_admin = MyUsers.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        client = APIClient()
        client.force_authenticate(user=user_admin)
        response = client.get('/api/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project(self):
        user_admin = MyUsers.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        # print(user)
        client = APIClient()
        client.force_authenticate(user=user_admin)
        project = Project.objects.create(name='https://vk.com/im?sel=218588853')
        user = MyUsers.objects.create(username='Step', email='Step@gmail.com')
        project.users.add(user)
        project.save()
        response = client.get(f'/api/project/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_project(self):
        user_admin = MyUsers.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        # print(user)
        client = APIClient()
        client.force_authenticate(user=user_admin)
        project = Project.objects.create(name='https://vk.com/im?sel=218588853')
        user = MyUsers.objects.create(username='Step', email='Step@gmail.com')
        project.users.add(user)
        project.save()
        response = client.put(f'/api/project/{project.id}/', {'name': 'https://stackoverflow.com/', 'users': user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
