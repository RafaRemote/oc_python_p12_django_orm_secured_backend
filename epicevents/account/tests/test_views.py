from django.test import TestCase
from users.models import EpicUser as User


class AccountAPITests(TestCase):
    """Class to test Account API endpoints"""    

    def test_sales_permission_on_account(self):
        """\u001b[45m Check sales permissions on account\u001b[0m"""
        User.objects.create_user(username="test_user", role="sales", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/account/").status_code == 200)

    def test_management_permission_on_account(self):
        """\u001b[45m Check management permissions on account\u001b[0m"""
        User.objects.create_user(username="test_user", role="management", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/account/").status_code == 403)
    
    def test_delete_method_on_account(self):
        """\u001b[45m Check delete method is forbidden on account\u001b[0m"""
        User.objects.create_user(username="test_user", role="sales", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.delete("/account/").status_code == 405)

