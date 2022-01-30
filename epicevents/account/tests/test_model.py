from django.apps import apps
from django.test import TestCase


class AccountModelTests(TestCase):
    """Class to test Account Model"""

    def test_is_there_an_account_model(self):
        """\033[1;33m Check There is a model Account\u001b[37m"""
        self.assertTrue(apps.get_model(app_label="account", model_name="Account"))
