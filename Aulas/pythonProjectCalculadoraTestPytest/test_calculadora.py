import pytest
import time

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b
class TestCalculadora:
    @pytest.mark.parametrize("a, b, resultado", [(1, 1, 2), (-1, 1, 0), (0, 0, 0)])
    def test_soma(self, a, b, resultado):
        start_time = time.time()
        assert soma(a, b) == resultado
        elapsed_time = time.time() - start_time
        print(f"\nTempo de Execução para test_soma: {elapsed_time:.6f} segundos")

    @pytest.mark.parametrize("a, b, resultado", [(3, 1, 2), (5, 5, 0), (0, 0, 0)])
    def test_subtracao(self, a, b, resultado):
        start_time = time.time()
        assert subtracao(a, b) == resultado
        elapsed_time = time.time() - start_time
        print(f"\nTempo de execução para test_subtracao: {elapsed_time:.6f} segundos")

    @pytest.mark.parametrize("a, b, resultado", [(2, 3, 6), (4, 0, 0), (-1, 5, -5)])
    def test_multiplicacao(self, a, b, resultado):
        start_time = time.time()
        assert multiplicacao(a, b) == resultado
        elapsed_time = time.time() - start_time
        print(f"\nTempo de execução para test_multiplicacao: {elapsed_time:.6f} segundos")

    @pytest.mark.parametrize("a, b, resultado", [(6, 3, 2), (8, 2, 4), (5, 2, 2.5)])
    def test_divisao(self, a, b, resultado):
        start_time = time.time()
        assert divisao(a, b) == resultado
        elapsed_time = time.time() - start_time
        print(f"\nTempo de execução para test_divisao: {elapsed_time:.6f} segundos")

    def test_divisao_por_zero(self):
        start_time = time.time()
        with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
            divisao(1, 0)
        elapsed_time = time.time() - start_time
        print(f"\nTempo de execução para test_divisao_por_zero: {elapsed_time:.6f} segundos")