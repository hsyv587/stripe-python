from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeMockTestCase


TEST_RESOURCE_ID = 'si_123'


class SubscriptionItemTest(StripeMockTestCase):
    def test_is_listable(self):
        resources = stripe.SubscriptionItem.list()
        self.assert_requested(
            'get',
            '/v1/subscription_items'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.SubscriptionItem)

    def test_is_retrievable(self):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/subscription_items/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.SubscriptionItem)

    def test_is_creatable(self):
        resource = stripe.SubscriptionItem.create(
            plan='plan',
            subscription='sub_123'
        )
        self.assert_requested(
            'post',
            '/v1/subscription_items'
        )
        self.assertIsInstance(resource, stripe.SubscriptionItem)

    # TODO: Fix this test
    # def test_is_saveable(self):
    #    resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
    #    resource.plan = 'plan'
    #    resource.save()
    #    self.assert_requested(
    #        'post',
    #        '/v1/subscription_items/%s' % resource.id,
    #        {
    #            'plan': 'plan',
    #        },
    #    )

    def test_is_modifiable(self):
        resource = stripe.SubscriptionItem.modify(
            TEST_RESOURCE_ID,
            plan='plan'
        )
        self.assert_requested(
            'post',
            '/v1/subscription_items/%s' % TEST_RESOURCE_ID,
            {
                'plan': 'plan',
            },
        )
        self.assertIsInstance(resource, stripe.SubscriptionItem)

    def test_is_deletable(self):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/subscription_items/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.SubscriptionItem)
