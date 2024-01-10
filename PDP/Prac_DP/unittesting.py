import unittest


class MyTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
        print(1+1)

    def test_subtraction(self):
        self.assertEqual(3 - 1, 2)

def test_1():
    print("run by pytest")
    
if __name__ == '__main__':
    unittest.main()
