import unittest
from unittest import TestSuite

from stats.Test_BFS import TestBFS
from stats.Test_Builder import TestBuilder
from stats.Test_Dm_Search import TestDmSearch
from stats.Test_Dm_Stats import TestDmStats
from stats.Test_Edges import TestEdges
from stats.Test_Graph_Finder import TestGraphFinder
from stats.Test_Helpers import TestHelpers
from stats.Test_Mediator import TestMediator
from stats.Test_Math import TestMath
from stats.Test_Stitch_Stats import TestStitchStats
from stats.Test_Simple_Search import TestSimpleSearch

class TestSuiteCases(object):
    def run_tests(self):
        suite = TestSuite()
        test_cases = (TestBFS, TestBuilder, TestDmSearch, TestDmStats,
                      TestEdges,
                      TestGraphFinder, TestHelpers, TestMath, TestMediator,
                      TestStitchStats, TestSimpleSearch)
        for test_class in test_cases:
            loaded_tests = unittest.defaultTestLoader.loadTestsFromTestCase(
                testCaseClass=test_class)
            suite.addTests(loaded_tests)

        runner = unittest.TextTestRunner()
        print(runner.run(suite))


if __name__ == '__main__':
    suite = TestSuiteCases()
    suite.run_tests()
