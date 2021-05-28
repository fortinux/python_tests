"""
[Ejemplo de test en Python]

Author: Fortinux
Date: [2021/05/27]
"""


def test_suma():
    assert sum([1, 1, 2, 3, 5, 8]) == 20, "Debe sumar 20"


if __name__ == "__main__":
    test_suma()
    print("Ha superado el test")
