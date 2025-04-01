import unittest

from tests.test_calculadora import TestCalculadora

suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)

runner = unittest.TextTestRunner()

result = runner.run(suite)
