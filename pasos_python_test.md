# Pasos python_tests
    
Creamos un ambiente virtual en nuestra máquina local e instalamos pip:
```   
python3 -m venv pythonTests
. pythonTests/bin/activate
python3 -m pip install --upgrade pip
```
Creamos un repositorio en Github y lo clonamos en nuestra máquina local:
```
git clone git@github.com:fortinux/python_tests.git
cd python_tests/
```
Creamos el primer fichero para verificar si puede pasar el test unitario:
```
vim test_suma.py
# Fichero test_suma.py
def test_suma():
    assert sum([1, 1, 2, 3, 5, 8]) == 20, "Debe sumar 20"

if __name__ == "__main__":
    test_suma()
    print("Ha superado el test")
```
Lo ejecutamos:

`python test_suma.py`

Si vamos a utilizar un workflow de CI/CD es conveniente instalar flake8 para analizar si nuestro código tiene errores:

```
pip install flake8
```
Lo configuramos:
```
pip freeze > requirements.txt
```
Lo ejecutamos con:

`flake8 --statistics`

Creamos otro ejemplo con dos pruebas unitarias:
```
vim test_suma2.py
def test_suma():
    assert sum([1, 1, 2, 3, 5, 8]) == 20, "Debe sumar 20"

def test_suma_tuple():
    assert sum((1, 1, 2, 3, 5, 8)) == 20, "Debe sumar 20"

if __name__ == "__main__":
    test_suma()
    test_suma_tuple()
    print("Ha superado los tests")
```
Lo ejecutamos:

`python test_suma2.py`

Creamos un ejemplo para utilizar unittest:
```
vim test_suma_unittest.py
# Fichero suma_unittest.py
import unittest


class TestSum(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sum([1, 1, 2, 3, 5, 8]), 20, "Debe sumar 20")

    def test_suma_tuple(self):
        self.assertEqual(sum((1, 1, 2, 3, 5, 8)), 20, "Debe sumar 20")


if __name__ == "__main__":
    unittest.main()
```
Lo ejecutamos con:

`python test_suma_unittest.py`

Instalamos nose2 para utilizarlo en las pruebas:
```
pip install nose2
```
Lo ejecutamos para analizar todos los ficheros del directorio actual que comienzan con test*.py:
```
python -m nose2
```
Creamos un fichero para hacer los tests con pytest:
```
vim test_suma_pytest.py
def test_suma():
    assert sum([1, 1, 2, 3, 5, 8]) == 20, "Debe sumar 20"


def test_suma_tuple():
    assert sum((1, 1, 2, 3, 5, 8)) == 20, "Debe sumar 20"
```
Lo ejecutamos con:
```
pytest
```
