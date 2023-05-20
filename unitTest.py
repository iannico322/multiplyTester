#!/usr/bin/env python3


import unittest

def mult(x, y):
    return float(x) * float(y)


class TestMult(unittest.TestCase):
    def test_mult_2positive_numbers(self):
        result = mult(3, 4)
        self.assertEqual(result, 12)

    def test_mult_2negative_numbers(self):
        result = mult(-2, -5)
        self.assertEqual(result, 10)

    def test_mult_2zero(self):
        result = mult(5, 0)
        self.assertEqual(result, 0)
        
    def test_mult_2string_numbers(self):
        result = mult("2", "5")
        self.assertEqual(result, 10)
    
           
if __name__ == '__main__':
    unittest.main()

