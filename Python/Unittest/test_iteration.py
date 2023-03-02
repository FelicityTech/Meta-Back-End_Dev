import unittest

class NumberTest(unittest.TestCase):

    def test_even(self):
     for i in range(0, 6):
        with self.subTest(i = i):
           self.assertEqual(i % 2, 0)
