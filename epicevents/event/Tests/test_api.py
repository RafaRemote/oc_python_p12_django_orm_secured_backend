from django.test import TestCase
from users.models import EpicUser as User


class EventAPITests(TestCase):
    """Class to test Event API endpoints"""

    def test_event_endpoint(self):
        """\u001b[45m Check There is an Event endpoint\u001b[0m"""
        self.assertTrue(self.client.get("/event/").status_code == 401)


    def test_app_event_logging(self):
        """\u001b[45m Check if logging for app event is done\u001b[0m"""
        User.objects.create_user(username="test_user", role="sales", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(open("event.log", "r"))
    