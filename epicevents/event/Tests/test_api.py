from django.test import TestCase


class EventAPITests(TestCase):
    """Class to test Event API endpoints"""

    def test_event_endpoint(self):
        """\u001b[45m Check There is an Event endpoint\u001b[0m"""
        self.assertTrue(self.client.get("/event/").status_code == 401)
