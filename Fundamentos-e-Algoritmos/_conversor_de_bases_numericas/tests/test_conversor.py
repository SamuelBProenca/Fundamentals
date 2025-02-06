import unittest
from src.conversor import convert_value

class TestConversor(unittest.TestCase):
    def test_binario_para_decimal(self):
        """Testa conversão de binário para decimal: 101 → 5"""
        self.assertEqual(convert_value("101", 1), '5')

    def test_decimal_para_binario(self):
        """Testa conversão de decimal para binário: 5 → 101"""
        self.assertEqual(convert_value("5", 2), '101')

    def test_decimal_para_hexadecimal(self):
        """Testa conversão de decimal para hexadecimal: 255 → FF"""
        self.assertEqual(convert_value("255", 3), 'FF')

    def test_hexadecimal_para_decimal(self):
        """Testa conversão de hexadecimal para decimal: 1A → 26"""
        self.assertEqual(convert_value("1A", 3), '26')

    def test_decimal_para_octal(self):
        """Testa conversão de decimal para octal: 10 → 12"""
        self.assertEqual(convert_value("10", 4), '12')

    def test_octal_para_decimal(self):
        """Testa conversão de octal para decimal: 12 → 10"""
        self.assertEqual(convert_value("12", 4), '10')

    def test_binario_para_hexadecimal(self):
        """Testa conversão de binário para hexadecimal: 101 → 5"""
        self.assertEqual(convert_value("101", 1), '5')

    def test_hexadecimal_para_binario(self):
        """Testa conversão de hexadecimal para binário: F → 1111"""
        self.assertEqual(convert_value("F", 3), '1111')

    def test_binario_para_octal(self):
        """Testa conversão de binário para octal: 101 → 5"""
        self.assertEqual(convert_value("101", 1), '5')

    def test_octal_para_binario(self):
        """Testa conversão de octal para binário: 5 → 101"""
        self.assertEqual(convert_value("5", 4), '101')

    def test_hexadecimal_para_octal(self):
        """Testa conversão de hexadecimal para octal: F → 17"""
        self.assertEqual(convert_value("F", 3), '17')

if __name__ == "__main__":
    unittest.main()
