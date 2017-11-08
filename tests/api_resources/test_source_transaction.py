from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeMockTestCase


class SourceTransactionTest(StripeMockTestCase):
    def test_is_listable(self):
        # TODO: remove stub once stripe-mock supports source_transactions
        self.stub_request(
            'get',
            '/v1/sources/src_123/source_transactions',
            {
                'object': 'list',
                'data': [{
                    'id': 'srxtxn_123',
                    'object': 'source_transaction',
                }],
            }
        )
        source = stripe.Source.construct_from({
            'id': 'src_123',
            'object': 'source'
        }, stripe.api_key)
        source_transactions = source.source_transactions()
        self.assert_requested(
            'get',
            '/v1/sources/src_123/source_transactions'
        )
        self.assertIsInstance(source_transactions.data, list)
        self.assertIsInstance(source_transactions.data[0],
                              stripe.SourceTransaction)
