import unittest

from tests.test_validacaoIdade import TestValidacaoIdade

suite = unittest.TestLoader().loadTestsFromTestCase(TestValidacaoIdade)

runner = unittest.TextTestRunner()

result = runner.run(suite)