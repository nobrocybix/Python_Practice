import unittest
from country_codes import get_country_code
from pygal_maps_world.i18n import COUNTRIES

class TestGetCountryCode(unittest.TestCase):
    def test_country_name_found(self):
        country_name = 'United States'
        self.assertEqual(get_country_code(country_name), 'us')

    def test_country_name_not_found(self):
        country_name = 'Invalid Country'
        self.assertIsNone(get_country_code(country_name))

    def test_country_name_none(self):
        country_name = None
        self.assertIsNone(get_country_code(country_name))

    def test_country_name_empty_string(self):
        country_name = ''
        self.assertIsNone(get_country_code(country_name))

if __name__ == '__main__':
    unittest.main()