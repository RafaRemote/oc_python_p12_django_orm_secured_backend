from django.test import TestCase
from users.models import EpicUser as User
from account.models import Account


class AccountAPITests(TestCase):
    """Class to test Account API endpoints"""

    def test_sales_permission_on_account(self):
        """\u001b[45m Check sales permissions on account\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/account/").status_code == 200)

    def test_management_permission_on_account(self):
        """\u001b[45m Check management permissions on account\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="management", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/account/").status_code == 403)

    def test_delete_method_on_account(self):
        """\u001b[45m Check delete method is forbidden on account\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.delete("/account/").status_code == 405)

    def test_account_search_and_filters_availabe(self):
        """\u001b[44m Check there are search and filters on account\u001b[0m"""
        user = User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        account = Account.objects.create(
            first_name="john", last_name="doe", email="john@doe.com", sales_contact=user
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        res = self.client.get("/account/?last_name=doe&email=")
        res2 = self.client.get("/account/?search=doe")
        self.assertTrue(account.email in res.content.decode())
        self.assertTrue(account.email in res2.content.decode())
