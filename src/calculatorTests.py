import unittest
from calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data_add = CsvReader('/src/Addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data_subtract = CsvReader('/src/Subtraction.csv').data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
