import random
import unittest
from collections import defaultdict
from itertools import product

from stats.Graph_View import PSearcher, PNode, PGraph
from stats.Stats_Graph_Mediator import StatsGraphMediator


class TestBFS(unittest.TestCase):
    def test_bfs(self):
        self.assertEqual(True, True)

    def test_add_edges(self):
        self.assertTrue(True)
        movies_row = list([1, 2, 3, 4])
        age_col = list([18, 19, 20, 21])
        movies_age_model = product(movies_row, age_col)

        mediator = StatsGraphMediator(movies_row, age_col)

        data_model = defaultdict(list)
        for movie, age in movies_age_model:
            if random.random() > 0.5:
                data_model[movie].append(age)

        mediator.mark_visited_nodes(data_model)

        graph = mediator.graph
        self.assertIsInstance(graph, PGraph)
        path_searcher = PSearcher(graph)
        path_searcher.add_edges()

        view_map = mediator.view_map
        self.assertIsInstance(view_map, dict)

        print('test_search')
        mediator.print_graph()
        list_nodes = graph.nodes

        bfs_generator = lambda n: path_searcher.bfs_search(n, graph)

        for start_node in list_nodes:
            self.assertIsInstance(start_node, PNode)
            DFS_nodes = path_searcher.dfs_search(start_node)

            BFS_nodes = list()
            if start_node.value is not None:
                generated_bfs = bfs_generator(start_node)
                for visited_node in generated_bfs:
                    self.assertIsInstance(visited_node, PNode)
                    BFS_nodes.append(visited_node)

            self.assertEqual(len(DFS_nodes), len(BFS_nodes))

            print('start_node: {}:{}:\tbfs_size = {}\tdfs_size = {}\n'
                  .format(start_node.coord.row, start_node.coord.col,
                          len(BFS_nodes), len(DFS_nodes)))


if __name__ == '__main__':
    unittest.main()
