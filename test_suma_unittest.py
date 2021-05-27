"""
[Ejemplo de dos tests en Python utilizando unittest]

Author: Fortinux
Date: [2020/05/27]
"""


import unittest


class TestSum(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sum([1, 1, 2, 3, 5, 8]), 20, "Debe sumar 20")

    def test_suma_tuple(self):
        self.assertEqual(sum((1, 1, 2, 3, 5, 8)), 20, "Debe sumar 20")


if __name__ == "__main__":
    unittest.main()
