from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError


class UsersManagersTests(TestCase):
    """
    Class to test user creation

    Methods
    -------
    test_create_user(sefl):
        creates user with valid arguments
        creates user with unvalid arguments
        multiple assertions checking expected result
    test_create_superuser(self):
        do the same as previoys method
    """

    def test_create_user(self):
        """Check models: create user"""
        User = get_user_model()
        user = User.objects.create_user(
            username="bob", role="support", password="1q2w#E$R"
        )
        self.assertEqual(user.username, "bob")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.role, "support")
        self.assertIsNotNone(user.username)
        self.assertIsNotNone(user.role)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username="")
        User.objects.create_user(username="", role="support", password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="bob", role="", password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", role="", password="foo")

    def test_create_superuser(self):
        """Check models: create superuser"""
        User = get_user_model()
        superadmin_user = User.objects.create_superuser(
            username="superadmin", password="1q2w#E$R"
        )
        self.assertEqual(superadmin_user.username, "superadmin")
        self.assertTrue(superadmin_user.is_active)
        self.assertTrue(superadmin_user.is_staff)
        self.assertNotEqual(superadmin_user.role, "support")
        self.assertIsNotNone(superadmin_user.username)
        with self.assertRaises(IntegrityError):
            User.objects.create_superuser(
                username="superadmin", password="foo"
            )
