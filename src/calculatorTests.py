import unittest
from calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)



if __name__ == '__main__':
    unittest.main()
