import unittest
from city_functions import get_city_country_name

class test_city_country(unittest.TestCase):
    def test_name(self):
        names = get_city_country_name('santiago', 'chile')
        self.assertEqual(names, 'Santiago, Chile')

unittest.main()