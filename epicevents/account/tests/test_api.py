from django.test import TestCase
from users.models import EpicUser as User


class AccountAPITests(TestCase):
    """Class to test Account API endpoints"""

    def test_account_endpoint(self):
        """\u001b[45m Check There is an Account endpoint\u001b[0m"""
        self.assertTrue(self.client.get("/account/").status_code == 401)

    def test_app_account_logging(self):
        """\u001b[45m Check if logging for app account is done\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(open("account.log", "r"))
