# File: test_check_numbers.py

import unittest


class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        print("printed in unittests")
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual(1, "1")


if __name__ == "__main__":
    unittest.main()

'''
.F
======================================================================
FAIL: test_str_float (__main__.CheckNumbers.test_str_float)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\HARI\Desktop\Sem3\PDP\Prac_sem\Testing\test_check_numbers.py", line 11, in test_str_float
    self.assertEqual(1, "1")
AssertionError: 1 != '1'

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=1)
'''