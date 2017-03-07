# -*- coding: utf-8 -*-
from django.test import TestCase
from item.models import Item


class ItemTests(TestCase):
    def test_hoge(self):
        item = Item(name="sample", price=100)
        actual = item.get_price_included_taxes()
        self.assertEqual(actual, 100)
