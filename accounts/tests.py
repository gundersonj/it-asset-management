from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="test user",
            email="test@email.com",
            password="testpass123",
        )
        self.admin = User.objects.create_superuser(
            username="admin user",
            email="admin@email.com",
            password="testpass123",
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, "test user")
        self.assertEqual(self.user.email, "test@email.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        self.assertEqual(self.admin.username, "admin user")
        self.assertEqual(self.admin.email, "admin@email.com")
        self.assertTrue(self.admin.is_active)
        self.assertTrue(self.admin.is_staff)
        self.assertTrue(self.admin.is_superuser)
