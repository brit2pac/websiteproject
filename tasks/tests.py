
from django.test import TestCase
from django.urls import reverse

from tasks.models import Position, Worker


class TaskManagerTests(TestCase):
    def setUp(self):
        position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testuser",
            password="testpassword123",
            position=position,
        )

    def test_task_list_redirects_anonymous_user(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, 302)

    def test_task_list_is_available_for_logged_in_user(self):
        self.client.login(
            username="testuser",
            password="testpassword123",
        )

        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, 200)
