import pytest
from partnero import CustomerAPI, Authentication
import responses


@pytest.fixture(scope="module")
def setup_authentication():
    Authentication.configure('test_api_token')


@pytest.fixture
def customer_api(setup_authentication):
    return CustomerAPI()


def test_create_customer_valid(customer_api):
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST, 'https://api.partnero.com/v1/customers', json={"status": "success"}, status=200)
        response = customer_api.create_customer('partner123', 'cust001', 'test@example.com', 'Test User')
        assert response['status'] == 'success'


def test_create_customer_invalid_email(customer_api):
    with pytest.raises(ValueError):
        customer_api.create_customer('partner123', 'cust001', 'not-an-email', 'Test User')
