import random
import unittest
from itertools import product

from collections import defaultdict

from stats.Graph_View import PSearcher, Coord, PGraph, PNode
from stats.Stats_Graph_Mediator import StatsGraphMediator, DataTuple


class TestEdges(unittest.TestCase):
    def test_mark_visited_graph(self):
        print()
        print('test_mark_visited_graph')
        movies_row = list([15, 20, 25, 30])
        age_col = list([18, 19, 20, 21])
        movies_age_model = product(movies_row, age_col)

        mediator = StatsGraphMediator(movies_row, age_col)

        print('Before marking visitors')
        mediator.print_graph()

        data_model = defaultdict(list)
        for movie, age in movies_age_model:
            if random.random() > 0.5:
                data_model[movie].append(age)

        print('After marking visitors')
        print('dict_items(num_movies, [age_group])')
        print(data_model.items())
        mediator.mark_visited_nodes(data_model)
        mediator.print_graph()

    def test_add_edges(self):
        self.assertTrue(True)
        movies_row = list([1,2,3,4])
        age_col = list([18, 19, 20, 21])
        movies_age_model = product(movies_row, age_col)

        mediator = StatsGraphMediator(movies_row, age_col)

        data_model = defaultdict(list)
        for movie, age in movies_age_model:
            if random.random() > 0.5:
                data_model[movie].append(age)

        mediator.mark_visited_nodes(data_model)

        graph = mediator.graph
        path_searcher = PSearcher(graph)
        path_searcher.add_edges()

        view_map = mediator.view_map
        self.assertIsInstance(view_map, dict)

        mediator.print_graph()

        list_visited_nodes = list()
        for row_data, list_col_data in data_model.items():
            for col_data in list_col_data:
                datatuple = DataTuple(row_data, col_data)
                coord = view_map.get(datatuple)
                self.assertIsInstance(coord, Coord)
                self.assertIsInstance(graph, PGraph)
                node_has_visitor = graph.get_node(coord)
                self.assertIsInstance(node_has_visitor, PNode)
                list_visited_nodes.append(node_has_visitor)

        for node in list_visited_nodes:
            print()
            self.assertIsInstance(node, PNode)
            list_children = graph.childrenOf(node)
            print('node_has_visitor\t\trow:col = {row}:{col}'.format(
                row=node.coord.row, col=node.coord.col))
            print('adjacent', end='\t')
            if len(list_children) is 0: print('no adjacent')
            for child_node in list_children:
                self.assertIsInstance(child_node, PNode)
                print('{}:{}'.format(child_node.coord.row,
                                     child_node.coord.col), end=',\t')
            print()

        print('test_search')
        mediator.print_graph()
        for node in list_visited_nodes:
            print()
            connected_nodes = path_searcher.dfs_search(node, list())
            print('start_node {}:{}:size = {}'.format(node.coord.row,
                                               node.coord.col, len(connected_nodes)))
            for cnode in connected_nodes:
                self.assertIsInstance(cnode, PNode)
                print('{}:{}'.format(cnode.coord.row, cnode.coord.col),
                      end=' , ')
            print()






if __name__ == '__main__':
    unittest.main()
