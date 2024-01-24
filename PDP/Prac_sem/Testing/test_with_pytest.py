# File: tests/test_with_pytest.py

def test_int_float():
    assert 1 == 1.0


class TestNumbers:
    def test_int_float(self):
        print("printed in unittests, not in pytest")

        assert 1 == 1.0

    def test_int_str(self):
        assert 1 == "1"

'''
HARI@LAP MINGW64 ~/Desktop/Sem3/PDP/Prac_sem (main)
$ python -m pytest
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.11.7, pytest-7.4.4, pluggy-1.3.0
rootdir: C:\Users\HARI\Desktop\Sem3\PDP\Prac_sem
plugins: Faker-21.0.0
collected 5 items

Testing\test_check_numbers.py .F                                                                                                                     [ 40%]
Testing\test_with_pytest.py ..F                                                                                                                      [100%] 

======================================================================== FAILURES ========================================================================= 
_______________________________________________________________ CheckNumbers.test_str_float _______________________________________________________________ 

self = <test_check_numbers.CheckNumbers testMethod=test_str_float>

    def test_str_float(self):
>       self.assertEqual(1, "1")
E       AssertionError: 1 != '1'

Testing\test_check_numbers.py:12: AssertionError
________________________________________________________________ TestNumbers.test_int_str _________________________________________________________________ 

self = <test_with_pytest.TestNumbers object at 0x0000021E56E6CE10>

    def test_int_str(self):
>       assert 1 == "1"
E       AssertionError: assert 1 == '1'

Testing\test_with_pytest.py:14: AssertionError
================================================================= short test summary info ================================================================= 
FAILED Testing/test_check_numbers.py::CheckNumbers::test_str_float - AssertionError: 1 != '1'
FAILED Testing/test_with_pytest.py::TestNumbers::test_int_str - AssertionError: assert 1 == '1'
=============================================================== 2 failed, 3 passed in 0.74s =============================================================== 
'''