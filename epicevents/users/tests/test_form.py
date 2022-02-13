from django.test import TestCase
from users.forms import EpicUserCreationForm
from users.models import EpicUser as User
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


class UserFormTests(TestCase):
    def test_group_assignment(self):
        """\033[1;42m Check groups assignement is correct \u001b[0m"""
        sales_team, c = Group.objects.get_or_create(name="sales_team")
        User = get_user_model()
        super_user = User.objects.create_superuser(username="jeanduc", password="1q2w#E$R")
        self.client.post(
            "/admin/login/", {"username": super_user.username, "password": "1q2w#E$R"}
        )
        res = self.client.post("/admin/users/epicuser/add/", data = {
            "username": "test_user",
            "role": "sales",
            "password1": "1q2w#E$R",
            "password2": "1q2w#E$R"
        })

        res = self.client.post(res.url, data = {
            "username": "test_user",
            "role": "sales"
        })
        test_user = User.objects.get(username="test_user")
        self.assertTrue(sales_team in test_user.groups.all())
