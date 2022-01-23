from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import EpicUser


class AdminPageTest(TestCase):
    """Class to test admin access page"""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        User.objects.create_superuser(
            username="jeanduc", role="management", password="1q2w#E$R"
        )
        User.objects.create_user(username="camille", role="sales", password="1q2w#E$R")
        User.objects.create_user(username="gerard", role="support", password="1q2w#E$R")

    def test_admin_page_is_accessible(self):
        """\033[1;35m Check admin page is accessible \033[1;37m"""
        res = self.client.get("/admin/login")
        self.assertIn("/admin/login/", res.url)

    def test_authorized_users_can_login(self):
        """\033[1;35m Check only managers can access admin site \u001b[37m"""
        super_user = EpicUser.objects.filter(role="management")[0]
        support_user = EpicUser.objects.filter(role="support")[0]
        sales_user = EpicUser.objects.filter(role="sales")[0]
        res = self.client.post(
            "/admin/login/", {"username": super_user.username, "password": "1q2w#E$R"}
        )
        self.assertNotIn("errornote", res.content.decode())
        res = self.client.post(
            "/admin/login/", {"username": support_user.username, "password": "1q2w#E$R"}
        )
        self.assertIn("errornote", res.content.decode())
        res = self.client.post(
            "/admin/login/", {"username": sales_user.username, "password": "1q2w#E$R"}
        )
        self.assertIn("errornote", res.content.decode())

    def test_admin_page_is_configured(self):
        """\033[1;35m Check admin page is configured \u001b[37m"""
        super_user = EpicUser.objects.filter(role="management")[0]
        res = self.client.post(
            "/admin/login/", {"username": super_user.username, "password": "1q2w#E$R"}
        )
        res = self.client.get("/admin/")
        self.assertIn("model-epicuser", res.content.decode())
