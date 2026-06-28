import pytest
from rsc.calculadora import Calculadora

class TestCalculadora:
    def test_soma_numeros_naturais(self):
        calculadora = Calculadora()
        assert calculadora.soma(1, 2) == 3
    
    def test_soma_numeros_inteiros(self):
        calculadora = Calculadora()
        assert calculadora.soma(-1, -2) == -3

