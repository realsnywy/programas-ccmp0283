import unittest
from tests.test_testProcessamento import TestProcessamento

suite = unittest.TestLoader().loadTestsFromTestCase(TestProcessamento)

runner = unittest.TextTestRunner()

result = runner.run(suite)
