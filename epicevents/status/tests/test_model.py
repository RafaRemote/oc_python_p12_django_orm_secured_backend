from django.apps import apps
from django.test import TestCase


class StatustModelTests(TestCase):
    """Class to test Status Model"""

    def test_is_there_an_status_model(self):
        """\033[1;33m Check There is a model Status\u001b[37m"""
        self.assertTrue(apps.get_model(app_label="status", model_name="Status"))
