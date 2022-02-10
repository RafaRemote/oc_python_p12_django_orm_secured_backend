from django.test import TestCase, Client

c = Client()


class ContractAPITests(TestCase):
    """Class to test Event API endpoints"""

    def test_contract_endpoint(self):
        """\u001b[45m Check There is a Contract endpoint\u001b[0m"""
        self.assertTrue(c.get("/contract/").status_code == 403)
