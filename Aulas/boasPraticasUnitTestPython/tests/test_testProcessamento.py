import unittest
from unittest.mock import MagicMock


class API:
    def get_data(self):
        pass

    def processar_dados_da_api(api):
        dados = api.get_data()
        return dados

    class TestProcessamento(unittest.TestCase):
        def test_processar_dados_da_api(self):
            mock_api = MagicMock()
            mock_api.get_data.return_value = {'valor': 42}
            resultado = processar_dados_da_api(mock_api)
            self.assertEqual(resultado, {'valor': 42})