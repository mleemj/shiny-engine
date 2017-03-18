import unittest
from unittest import TestSuite

from stats.Test_Builder import TestBuilder
from stats.Test_Dm_Search import TestDmSearch
from stats.Test_Dm_Stats import TestDmStats
from stats.Test_Edges import TestEdges
from stats.Test_Graph_Finder import TestGraphFinder
from stats.Test_Helpers import TestHelpers
from stats.Test_Mediator import TestMediator


class TestSuiteCases(object):
    def run_tests(self):
        suite = TestSuite()
        test_cases = (TestBuilder, TestDmSearch, TestDmStats, TestEdges,
                      TestGraphFinder, TestHelpers, TestMediator)
        for test_class in test_cases:
            loaded_tests = unittest.defaultTestLoader.loadTestsFromTestCase(
                testCaseClass=test_class)
            suite.addTests(loaded_tests)

        runner = unittest.TextTestRunner()
        print(runner.run(suite))


if __name__ == '__main__':
    suite = TestSuiteCases()
    suite.run_tests()
