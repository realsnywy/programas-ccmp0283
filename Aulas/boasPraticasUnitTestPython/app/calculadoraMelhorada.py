import unittest

from tests.test_calculadoraMelhorada import TestCalculadoraMelhorada

suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadoraMelhorada)

runner = unittest.TextTestResult()

result = runner.run(suite)
