import unittest


def validar_idade(idade):
    if idade < 0:
        raise ValueError("A idade não pode ser negativa")
    elif idade < 18:
        return "Menor de idade"
    else:
        return "Maior de idade"


class TestValidacaoIdade(unittest.TestCase):
    def test_idade_positiva_menor(self):
        resultado = validar_idade(15)
        self.assertEqual(resultado, "Menor de idade")

    def test_idade_positiva_maior(self):
        resultado = validar_idade(25)
        self_assertEqual(resultado, "Maior de idade")

    def test_idade_zero(self):
        resultado = validar_idade(0)
        self.assertEqual(resultado, "Menor de idade")

    def test_idade_negativa(self):
        with self.assertRaises(ValueError):
            validar_idade(-10)
