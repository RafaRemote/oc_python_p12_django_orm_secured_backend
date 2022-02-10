from django.test import TestCase, Client

c = Client()


class EventAPITests(TestCase):
    """Class to test Event API endpoints"""

    def test_event_endpoint(self):
        """\u001b[45m Check There is an Event endpoint\u001b[0m"""
        self.assertTrue(c.get("/event/").status_code == 403)
