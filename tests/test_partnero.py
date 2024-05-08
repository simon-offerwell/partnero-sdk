import unittest
from partnero import CustomerAPI, Authentication


class TestCustomerAPI(unittest.TestCase):
    def setUp(self):
        self.api = CustomerAPI(auth=Authentication(api_token="test"))

    def test_create_customer_valid(self):
        # Assuming responses or a similar library is used to mock HTTP responses
        with responses.RequestsMock() as rsps:
            rsps.add(rsps.POST, 'https://api.partnero.com/v1/customers', json={"status": "success"}, status=200)
            response = self.api.create_customer('partner123', 'cust001', 'test@example.com', 'Test User')
            self.assertEqual(response['status'], 'success')

    def test_create_customer_invalid_email(self):
        with self.assertRaises(ValueError):
            self.api.create_customer('partner123', 'cust001', 'not-an-email', 'Test User')
