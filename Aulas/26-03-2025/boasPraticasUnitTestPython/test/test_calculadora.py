import unittest


def soma(a, b):
    return a + b


class TestCalculadora(unittest.TestCase):
    def test_soma_positivos(self):
        resultado = soma(2, 3)
        self.assertEqual(resultado, 5)

    def test_soma_negativos(self):
        resultado = soma(-5, -7)
        self.assertEqual(resultado, -12)

    def test_soma_zero(self):
        resultado = soma(0, 0)
        self.assertEqual(resultado, 0)
