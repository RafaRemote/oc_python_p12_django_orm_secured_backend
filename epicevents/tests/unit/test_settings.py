from django.test import TestCase
from django.db import connection
import django


class SettingsTestCase(TestCase):
    """Class to test dependencies versions"""

    def test_django_version_is_at_least_3(self):
        """Checks if Django version is greater or equal than 3"""
        self.assertGreaterEqual(django.VERSION[0], 3)

    def test_python_version_is_three(self):
        """
        Checks if Python version is 3
        if Django version is at least 3 then the app use Python 3
        https://docs.djangoproject.com/en/4.0/faq/install/

        """
        self.assertGreaterEqual(django.VERSION[0], 3)

    def test_postgresql_version(self):
        """Checks if PostgreSQL version is greater or equal to 12.0"""
        self.assertGreaterEqual(connection.cursor().connection.server_version, 120000)
