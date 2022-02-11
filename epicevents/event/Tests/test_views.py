from django.test import TestCase
from users.models import EpicUser as User
from event.models import Event
from account.models import Account
from status.models import Status


class EventAPITests(TestCase):
    """Class to test Event API endpoints"""

    def test_sales_permission_on_event(self):
        """\u001b[45m Check sales permissions on event\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/event/").status_code == 403)

    def test_management_permission_on_event(self):
        """\u001b[45m Check management permissions on event\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="management", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/event/").status_code == 403)

    def test_support_permission_on_event(self):
        """\u001b[45m Check support permissions on event\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="support", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/event/").status_code == 200)

    def test_post_on_event_is_forbidden(self):
        """\u001b[45m Check post/delete event are 405 method not allowed\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="support", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.post("/event/", {}).status_code == 405)
        self.assertTrue(self.client.delete("/event/1/").status_code == 405)

    def test_event_search_and_filters_availabe(self):
        """\u001b[44m Check there are search and filters on event\u001b[0m"""
        user = User.objects.create_user(
            username="test_user", role="support", password="1q2w#E$R"
        )
        Status.objects.create(status="planning")
        account = Account.objects.create(
            first_name="john", last_name="doe", email="john@doe.com", sales_contact=user
        )
        Event.objects.create(support_contact=user, account=account)
        self.client.login(username="test_user", password="1q2w#E$R")
        res = self.client.get(
            "/event/?account__last_name=doe&account__email=&date_created="
        )
        res2 = self.client.get("/event/?search=doe")
        self.assertTrue("john doe" in res.content.decode())
        self.assertTrue("john doe" in res2.content.decode())
