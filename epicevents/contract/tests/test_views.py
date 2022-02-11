from django.test import TestCase
from users.models import EpicUser as User


class ContractAPITests(TestCase):
    """Class to test Contract API endpoints"""    

    def test_management_permission_on_contract(self):
        """\u001b[45m Check management permissions on contract\u001b[0m"""
        User.objects.create_user(username="test_user", role="management", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/contract/").status_code == 403)

    def test_delete_method_on_contract(self):
        """\u001b[45m Check contract delete method forbidden\u001b[0m"""
        User.objects.create_user(username="test_user", role="sales", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.delete("/contract/").status_code == 405)
