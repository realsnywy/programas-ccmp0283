import unittest


def adicionar(a, b):
    return a + b


class TestCalculadoraMelhorada(unittest.TestCase):
    def test_adicionar_numeros_positivos(self):
        resultado = adicionar(2, 3)
        self.assertEqual(resultado, 5)

    def test_adicionar_numeros_negativos(self):
        resultado = adicionar(-5, -7)
        self.assertEqual(resultado, -12)

    def test_adicionar_numero_positivo_e_negativo(self):
        resultado = adicionar(10, -5)
        self.assertEqual(resultado, 5)
