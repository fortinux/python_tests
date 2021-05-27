"""
[Ejemplo de dos tests en Python]

Author: Fortinux
Date: [2020/05/27]
"""


def test_suma():
    assert sum([1, 1, 2, 3, 5, 8]) == 20, "Debe sumar 20"


def test_suma_tuple():
    assert sum((1, 1, 2, 3, 5, 8)) == 20, "Debe sumar 20"


if __name__ == "__main__":
    test_suma()
    test_suma_tuple()
    print("Ha superado los tests")
