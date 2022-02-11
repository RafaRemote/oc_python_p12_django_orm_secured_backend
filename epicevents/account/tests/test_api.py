from django.test import TestCase, Client

c = Client()


class AccountAPITests(TestCase):
    """Class to test Account API endpoints"""    

    def test_account_endpoint(self):
        """\u001b[45m Check There is an Account endpoint\u001b[0m"""
        self.assertTrue(c.get("/account/").status_code == 401)
