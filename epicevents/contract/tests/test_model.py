from django.apps import apps
from django.test import TestCase


class ContractModelTests(TestCase):
    """Class to test Contract Model"""

    def test_is_there_a_contract_model(self):
        """\033[1;33m Check There is a model Contrat\u001b[37m"""
        self.assertTrue(apps.get_model(app_label="contract", model_name="Contract"))

