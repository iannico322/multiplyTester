#!/usr/bin/env python3


import unittest

class CustomError(Exception):
    pass


def mult(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return "gay you input string"
    return x * y
 



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
        
    def test_mult_2strings(self):
        result = mult("5", "0")
        self.assertEqual(result,"gay you input string")
  
 
           
if __name__ == '__main__':
    unittest.main()

