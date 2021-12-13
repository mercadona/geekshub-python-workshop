import unittest
from decimal import Decimal

from implementation import Cart


def get_catalog():
    return {
        'Lechuga corazón romana': Decimal('1.00'),
        'Patas de pulpo cocido': Decimal('8.95'),
        'Salmón marinado Hacendado': Decimal('2.35'),
    }


class TestCartTotalPrice(unittest.TestCase):

    def test_returns_zero_when_cart_empty(self):
        cart = Cart(catalog=[])

        self.assertEqual(cart.total_price(), Decimal('0.00'))

    def test_returns_sum_of_prices_when_quantity_greater_than_one(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana', quantity=2)

        self.assertEqual(cart.total_price(), Decimal('2.00'))

    def test_returns_sum_of_prices_when_multiple_products_in_cart(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana')
        cart.add('Salmón marinado Hacendado')

        self.assertEqual(cart.total_price(), Decimal('3.35'))


class TestCartAdd(unittest.TestCase):

    def test_adds_qty_one_when_product_in_catalog_and_no_qty_given(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana')

        self.assertEqual(cart.total_price(), Decimal('1.00'))

    def test_adds_given_qty_when_product_in_catalog_and_qty_given(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana', quantity=3)

        self.assertEqual(cart.total_price(), Decimal('3.00'))

    def test_sums_qtys_when_adding_multiple_times(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana')
        cart.add('Lechuga corazón romana')

        self.assertEqual(cart.total_price(), Decimal('2.00'))

    def test_raises_valueerror_when_product_not_in_catalog(self):
        cart = Cart(catalog=get_catalog())
        with self.assertRaises(ValueError):
            cart.add('no existo')


class TestCartRemove(unittest.TestCase):

    def test_removes_qty_one_when_product_in_cart_and_no_qty_given(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana', quantity=2)
        cart.remove('Lechuga corazón romana')

        self.assertEqual(cart.total_price(), Decimal('1.00'))

    def test_removes_product_when_last_remaining_quantity(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana')
        cart.remove('Lechuga corazón romana')

        self.assertEqual(cart.total_price(), Decimal('0.00'))

    def test_removes_given_qty_when_product_in_cart_and_qty_given(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana', quantity=3)
        cart.remove('Lechuga corazón romana', quantity=2)

        self.assertEqual(cart.total_price(), Decimal('1.00'))

    def test_raises_valueerror_when_product_not_in_cart(self):
        cart = Cart(catalog=get_catalog())
        with self.assertRaises(ValueError):
            cart.remove('Lechuga corazón romana')

    def test_raises_valueerror_when_given_qty_greater_than_in_cart(self):
        cart = Cart(catalog=get_catalog())
        cart.add('Lechuga corazón romana', quantity=2)

        with self.assertRaises(ValueError):
            cart.remove('Lechuga corazón romana', quantity=3)


if __name__ == '__main__':
    unittest.main()
