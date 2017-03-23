import unittest

from Max_Sales_Strategy import MaxSalesStrategy
from stats.Graph_View import PNode


class TestMaxSalesStrategy(unittest.TestCase):
    def test_strategy(self):
        self.assertEqual(True, True)
        maxSales = MaxSalesStrategy()
        generated_nodes = maxSales.get_list_combinations()

        for node in generated_nodes:
            self.assertIsInstance(node, PNode)
            print('{}'.format(node.value))


if __name__ == '__main__':
    unittest.main()
