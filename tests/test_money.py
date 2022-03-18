from international_data_preprocessing import Money, country_to_primary_currency, parse_money
import unittest

class TestMoney(unittest.TestCase):
    
    def test_get(self):
        c = Money(55, 'USD', 'United States Dollars')
        self.assertEqual(c.get('amount'), 55)
        self.assertEqual(c.get('full'), 'United States Dollars')
        self.assertEqual(c.get('abbv'), 'USD')

    def test_get_invalid_input(self):
        pass

    def test_get_empty_field(self):
        pass

    def test_parse(self):
        pass

    def test_parse_large_data(self):
        pass

    def test_parse_invalid_input(self):
        pass

    def test_country_to_primary_currency(self):
        pass

    def test_country_to_primary_currency_large_data(self):
        pass

    def test_country_to_primary_currency_invalid_input(self):
        pass

    def test_parse_money(self):
        pass

    def test_parse_money_large_data(self):
        pass

    def test_parse_money_invalid_input(self):
        pass


if __name__ == '__main__':
    unittest.main()