from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeMockTestCase


TEST_RESOURCE_ID = 'sku_123'


class SKUTest(StripeMockTestCase):
    def test_is_listable(self):
        resources = stripe.SKU.list()
        self.assert_requested(
            'get',
            '/v1/skus'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.SKU)

    def test_is_retrievable(self):
        resource = stripe.SKU.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/skus/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.SKU)

    def test_is_creatable(self):
        resource = stripe.SKU.create(
            currency='usd',
            inventory=dict(
                type='finite',
                quantity=500
            ),
            price=100,
            product='prod_123'
        )
        self.assert_requested(
            'post',
            '/v1/skus'
        )
        self.assertIsInstance(resource, stripe.SKU)

    def test_is_saveable(self):
        resource = stripe.SKU.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/skus/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.SKU.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/skus/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.SKU)

    def test_is_deletable(self):
        resource = stripe.SKU.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/skus/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.SKU)
