from django.test import TestCase
from users.models import EpicUser as User
from contract.models import Contract
from account.models import Account


class ContractAPITests(TestCase):
    """Class to test Contract API endpoints"""

    def test_management_permission_on_contract(self):
        """\u001b[45m Check management permissions on contract\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="management", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/contract/").status_code == 403)

    def test_delete_method_on_contract(self):
        """\u001b[45m Check contract delete method forbidden\u001b[0m"""
        User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.delete("/contract/").status_code == 405)

    def test_contract_search_and_filters_availabe(self):
        """\u001b[44m Check there are search and filters on contract\u001b[0m"""
        user = User.objects.create_user(
            username="test_user", role="sales", password="1q2w#E$R"
        )
        account = Account.objects.create(
            first_name="john", last_name="doe", email="john@doe.com", sales_contact=user
        )
        Contract.objects.create(
            account=account, amount="1000", payment_due="2030-10-10", sales_contact=user
        )
        self.client.login(username="test_user", password="1q2w#E$R")
        res = self.client.get(
            "/contract/?account__last_name=&account__email=&date_created=&amount=1000"
        )
        res2 = self.client.get("/contract/?search=doe")
        self.assertTrue("1000" in res.content.decode())
        self.assertTrue("john doe" in res2.content.decode())
