from django.test import TestCase
from users.models import EpicUser as User


class EventAPITests(TestCase):
    """Class to test Event API endpoints"""    

    def test_sales_permission_on_event(self):
        """\u001b[45m Check sales permissions on event\u001b[0m"""
        User.objects.create_user(username="test_user", role="sales", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/event/").status_code == 403)

    def test_management_permission_on_event(self):
        """\u001b[45m Check management permissions on event\u001b[0m"""
        User.objects.create_user(username="test_user", role="management", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/event/").status_code == 403)

    def test_support_permission_on_event(self):
        """\u001b[45m Check support permissions on event\u001b[0m"""
        User.objects.create_user(username="test_user", role="support", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/event/").status_code == 200)

    def test_post_on_event_is_forbidden(self):
        """\u001b[45m Check post/delete event are 405 method not allowed\u001b[0m"""
        User.objects.create_user(username="test_user", role="support", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.post("/event/", {}).status_code == 405)
        self.assertTrue(self.client.delete("/event/1/").status_code == 405)
