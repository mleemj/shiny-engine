import unittest

from numpy import random as npr, arange

from stats.Stats_Graph_Mediator import StatsGraphMediator
from stats.Graph_View import PGraph, PNode


class TestGraphFinder(unittest.TestCase):
    def test_dfs_search(self):
        self.assertTrue(True)
        row_model = arange(start=0, stop=4, step=1).tolist()
        col_model = arange(start=0, stop=4, step=1).tolist()
        mediator = StatsGraphMediator(row_model,col_model)
        data_model = dict()

        for row in row_model:
            col_list = list()
            for col in col_model:
                randvalue = npr.randint(low=0, high=2)
                has_visitor = True if randvalue is 1 else False
                if has_visitor is True:
                    col_list.append(col)
            data_model[row] = col_list

        print()
        mediator.mark_visited_nodes(data_model)
        graph = mediator.graph
        self.assertIsInstance(graph, PGraph)
        list_visited_nodes = list()
        for node in graph.nodes:
            self.assertIsInstance(node, PNode)
            if node.has_visitor:
                list_visited_nodes.append(node)

        for node in list_visited_nodes:
            print('{}:{}:{}'.format(node.coord.row, node.coord.col,
                                    node.has_visitor))
            self.assertTrue(node.has_visitor)
        mediator.print_graph()


if __name__ == '__main__':
    unittest.main()
