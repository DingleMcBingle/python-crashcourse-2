import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests the function city_country"""
    def test_city_country(self):
        pair = city_country('Altoona','Usa')
        self.assertEqual(pair,'Altoona, Usa')
        
unittest.main()