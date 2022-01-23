from django.test import TestCase
from django.db import connection
import django


class SettingsTestCase(TestCase):
    """Class to test dependencies versions"""

    def test_django_version_is_at_least_3(self):
        """\033[1;34m Check Django version 3.0+\u001b[37m"""
        self.assertGreaterEqual(django.VERSION[0], 3)

    def test_python_version_is_three(self):
        """
        \033[1;34m Check Python version 3\u001b[37m
        if Django version is at least 3 then the app use Python 3
        https://docs.djangoproject.com/en/4.0/faq/install/

        """
        self.assertGreaterEqual(django.VERSION[0], 3)

    def test_postgresql_version(self):
        """\033[1;34m Check PostgreSQL version 12.0+\u001b[37m"""
        self.assertGreaterEqual(connection.cursor().connection.server_version, 120000)
