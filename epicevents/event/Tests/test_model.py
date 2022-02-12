from django.apps import apps
from django.test import TestCase


class EventModelTests(TestCase):
    """Class to test Event Model"""

    def test_is_there_an_event_model(self):
        """\033[1;33m Check There is a model Event\u001b[37m"""
        self.assertTrue(apps.get_model(app_label="event", model_name="Event"))
