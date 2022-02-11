from django.test import TestCase
from users.models import EpicUser as User


class ContractAPITests(TestCase):
    """Class to test Event API endpoints"""

    def test_contract_endpoint(self):
        """\u001b[45m Check There is a Contract endpoint\u001b[0m"""
        self.assertTrue(self.client.get("/contract/").status_code == 401)

    def test_app_contract_logging(self):
        """\u001b[45m Check if logging for app contract is done\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(open("contract.log", "r"))
