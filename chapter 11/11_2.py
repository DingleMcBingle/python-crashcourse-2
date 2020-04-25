import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests the function city_country"""

    def test_city_country(self):
        pair = city_country('pittsburgh', 'usa')
        self.assertEqual(pair, 'Pittsburgh, Usa')

    def test_city_country_population(self):
        pair = city_country('pittsburgh', 'usa', population=301048)
        self.assertEqual(pair, 'Pittsburgh, Usa - Population: 301048')

unittest.main()