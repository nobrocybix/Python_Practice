import unittest
import country_codes

from pygal_maps_world.i18n import COUNTRIES

class test_codes(unittest.TestCase):

    def setUp(self):

        self.country_name = "Hong Kong"

    def test_country_code(self):

        code = country_codes.get_country_code(self.country_name)
        self.assertIn(code, COUNTRIES.keys())


unittest.main()