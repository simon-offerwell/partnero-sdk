from .base_api import BaseAPI


class TransactionAPI(BaseAPI):
    def list_transactions(self, limit: int = 15, page: int = 1) -> dict:
        params = {'limit': limit, 'page': page}
        return self.send_request('GET', 'transactions', params=params)

    def create_transaction(self, customer_key: str, amount: float, action: str, transaction_key: str = None, product_id: str = None, product_type: str = None) -> dict:
        data = {
            'customer': {'key': customer_key},
            'key': transaction_key,
            'amount': amount,
            'product_id': product_id,
            'product_type': product_type,
            'action': action
        }
        return self.send_request('POST', 'transactions', data=data)

    def delete_transaction(self, transaction_key: str) -> dict:
        return self.send_request('DELETE', f'transactions/{transaction_key}')


"""
{
    "customer": {
        "key": "simontest3@offerwell.com"
    },
    "key": "transaction_123546",
    "amount": 19.99,
    "action": "per-listing"
}
"""