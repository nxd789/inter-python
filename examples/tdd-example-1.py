# example TDD code

def add(x,y):
    return x+y

import unittest

class AdditionTests(unittest.TestCase):

    def test_addition(self):
        assert add(1,2) == 3

    def test_float_addition(self):
        assert -0.00001 < (add(0.66666, 0.33333) - 0.99999) < 0.00001

if __name__ == "__main__":
    unittest.main()

