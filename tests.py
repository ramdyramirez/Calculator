import unittest
from main import Add


class TestCalculatorMethods(unittest.TestCase):

    def test_comma_delimiter(self):
        self.assertEqual(Add('1,2,5'), 8)

    def test_newline_input(self):
        self.assertEqual(Add('1\n,2,3'), 6)
        self.assertEqual(Add('1,\n2,4'), 7)

    def test_custom_delimiter(self):
        self.assertEqual(Add('//;\n1;3;4'), 8)
        self.assertEqual(Add('//$\n1$2$3'), 6)
        self.assertEqual(Add('//@\n2@3@8'), 13)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            Add('//@\n2@3@-8')

    def test_numbers_lg_1000(self):
        self.assertEqual(Add('2,1001'), 2)

if __name__ == "__main__":
    unittest.main()