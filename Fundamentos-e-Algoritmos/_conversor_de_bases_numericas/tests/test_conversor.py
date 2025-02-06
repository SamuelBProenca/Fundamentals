import unittest 
from src.conversor import conversor

class TestConversor(unittest.TestCase):
    def binario_para_decimal(self):
        self.assertEqual(conversor(1, "1010"), 10)

