import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.adam = Employee('adam', 'mason', 65000)

    def test_give_default_raise(self):
        self.adam.give_raise()
        self.assertEqual(self.adam.salary, 70000)

    def test_give_custom_raise(self):
        self.adam.give_raise(10000)
        self.assertEqual(self.adam.salary, 75000)

unittest.main()