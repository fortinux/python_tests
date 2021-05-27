[![Python application](https://github.com/fortinux/python_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/fortinux/python_tests/actions/workflows/python-app.yml)
# python_tests    
En este repositorio he creado algunos ejemplos para ejecutar tests en Python usando unittest, nose2 y pytest https://docs.pytest.org/en/latest/ en un ambiente virtual.    
    
Los pasos para reproducirlos se encuentran en el fichero pasos_python_test.md   
      
En Github he agregado el workflow "Python application".     
Al ejecutarse daba el siguiente error:    
ERROR: Could not find a version that satisfies the requirement pkg-resources==0.0.0    
    
Para resolverlo he eliminado del fichero requirements.txt:    
pkg-resources==0.0.0    
    
