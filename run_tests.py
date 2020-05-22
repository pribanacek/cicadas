import unittest

from tests.unit.TestCLI import TestCLI
from tests.unit.TestParsing import TestParsing
from tests.unit.TestTopology import TestTopology
from tests.unit.TestOutput import TestOutput

import src.util.Logging as Logging

Logging.silent = True

def suite():
    suite = unittest.TestSuite()
    tests = [TestCLI, TestParsing, TestTopology, TestOutput]
    for test in tests:
        suite.addTests(unittest.makeSuite(test))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
