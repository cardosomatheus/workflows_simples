import pytest
from rsc.calculadora import Calculadora

class TestCalculadora:
    def test_soma_numeros_naturais(self):
        calculadora = Calculadora()
        assert calculadora.soma(1, 2) == 3
    
    def test_soma_numeros_inteiros(self):
        calculadora = Calculadora()
        assert calculadora.soma(-1, -2) == -3

    def test_subtracao_numeros_naturais(self):
        calculadora = Calculadora()
        assert calculadora.subtracao(1, 2) == -1
    
    def test_subtracao_numeros_inteiros(self):
        calculadora = Calculadora()
        assert calculadora.subtracao(-1, -2) == 1

