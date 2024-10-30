import unittest
from population import get_city_country_name

class test_city_country(unittest.TestCase):
    def test_name(self):
        names = get_city_country_name('santiago', 'chile', 5000000)
        self.assertEqual(names, 'Santiago, Chile - population 5000000')

unittest.main()