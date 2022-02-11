from django.test import TestCase
from users.models import EpicUser as User


class MonitoringAPITests(TestCase):
    """Class to test monitoring is done for the app"""

    def test_monitoring(self):
        """\u001b[45m Check There is a monitoring section on admin site\u001b[0m"""
        User.objects.create_user(username="test_user", role="management", password="1q2w#E$R")
        self.client.login(username="test_user", password="1q2w#E$R")
        self.assertTrue(self.client.get("/admin/drf_api_logger/apilogsmodel/").status_code == 200)
