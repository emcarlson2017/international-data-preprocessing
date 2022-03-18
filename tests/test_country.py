from international_data_preprocessing import Country, parse_countries
import unittest

class TestCountry(unittest.TestCase):
    
    def test_get(self):
        c = Country('US', 'USA', '001', 'United States of America', 'United States')
        self.assertEqual(c.get('alpha2'), 'US')
        self.assertEqual(c.get('alpha3'), 'USA')
        self.assertEqual(c.get('UN'), '001')
        self.assertEqual(c.get('full'), 'United States of America')
        self.assertEqual(c.get('short'), 'United States')

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

    def test_parse_countries(self):
        pass

    def test_parse_countries_large_data(self):
        pass

    def test_parse_countries_invalid_input(self):
        pass


if __name__ == '__main__':
    unittest.main()