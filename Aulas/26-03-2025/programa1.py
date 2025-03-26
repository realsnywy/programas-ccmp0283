import unittest


class TestExemplo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_soma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)

    def test_subtracao(self):
        resultado = 5 - 3
        self.assertEqual(resultado, 2)


if __name__ == "__main__":
    unittest.main()
