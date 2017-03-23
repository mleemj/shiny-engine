import random
import unittest
from collections import defaultdict
from itertools import product

from stats.Graph_View import PSearcher, PNode, PGraph, Coord
from stats.Stats_Graph_Mediator import StatsGraphMediator

from stats.Stitch_Stats import SalesItem, SalesItemByAge, SalesStats


class TestStitchStats(unittest.TestCase):
    def test_curate_collection(self):
        age_group_18 = list([18, 19, 20, 21])
        age_group_22 = list([22, 23, 24, 25])
        age_group_26 = list([26, 27, 28, 29])

        col_model = list()
        for col_index in range(5):
            revenue = random.randint(1, 5)
            item = SalesItem(col_index, revenue)
            col_model.append(item)

        self.build_new_graph(age_group_18, col_model)
        self.build_new_graph(age_group_22, col_model)
        self.build_new_graph(age_group_26, col_model)

    def build_new_graph(self, row_model, col_model):
        stats = SalesStats()
        for age in row_model:
            salesItemByAge = SalesItemByAge(age)
            for item in col_model:
                if random.random() > 0.5:
                    salesItemByAge.add_item(item)
            stats.add_sales_item_age(salesItemByAge)

        mediator = StatsGraphMediator(data_row = row_model,
                                      data_col = col_model)
        mediator.mark_nodes(stats.data_model)

        graph = mediator.graph
        self.assertIsInstance(graph, PGraph)
        path_searcher = PSearcher(graph)
        path_searcher.add_edges()

        list_nodes = graph.nodes
        test_print_graph(graph, row_model, col_model)
        most_connected_nodes = 0
        all_connected_nodes = dict()
        for start_node in list_nodes:
            self.assertIsInstance(start_node, PNode)
            DFS_nodes = path_searcher.dfs_search(start_node)
            found_connected_nodes = len(DFS_nodes)
            if found_connected_nodes > most_connected_nodes:
                most_connected_nodes = found_connected_nodes
            if len(DFS_nodes) is not 0: all_connected_nodes[start_node] = DFS_nodes

        most_revenue = 0
        for connected_nodes in all_connected_nodes.values():
            revenue = 0
            for node in connected_nodes:
                self.assertIsInstance(node, PNode)
                item_index = node.coord.col
                salesItem = col_model[item_index]
                self.assertIsInstance(salesItem, SalesItem)
                revenue = revenue + salesItem.revenue
            if revenue > most_revenue: most_revenue = revenue

        print('Most connected area = {}'.format(most_connected_nodes))
        print('Most revenue = {}\n\n'.format(most_revenue))



    def setUp(self):
        num_items = 4
        self.list_item_cols = list()
        for col_index in range(num_items):
            revenue = random.randint(1, 5)
            item = SalesItem(col_index, revenue)
            self.list_item_cols.append(item)

        self.list_age_rows = list([18, 19, 20, 21])
        stats = SalesStats()
        for age in self.list_age_rows:
            salesItemByAge = SalesItemByAge(age)
            for item in self.list_item_cols:
                if random.random() > 0.5:
                    salesItemByAge.add_item(item)
            stats.add_sales_item_age(salesItemByAge)

        data_model = stats.data_model

        mediator = StatsGraphMediator(data_row=self.list_age_rows,
                                      data_col=self.list_item_cols)
        mediator.mark_nodes(data_model)

        self.graph = mediator.graph
        self.assertIsInstance(self.graph, PGraph)
        path_searcher = PSearcher(self.graph)
        path_searcher.add_edges()

        view_map = mediator.view_map
        self.assertIsInstance(view_map, dict)

        list_nodes = self.graph.nodes

        bfs_generator = lambda n: path_searcher.bfs_search(n, self.graph)

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


def test_print_graph(graph, row_model, col_model):
    for row_index in range(len(row_model)):
        end_row = '\t\t\t\t'
        print('row = {}'.format(row_index), end=end_row)
        for col_index in range(len(col_model)):
            coord = Coord(row=row_index, col=col_index)
            node = graph.get_node(coord)
            assert isinstance(node, PNode)
            if node.value is not None:
                print(1, end='\t')
            else:
                print(0, end='\t')
        print('age = {}'.format(row_model[row_index]))

    print('\ncol = ', end='\t\t\t\t')
    for col_index in range(len(col_model)):
        print('{}'.format(col_index), end='\t')

    print('\nrev = ', end='\t\t\t\t')
    for col_index in range(len(col_model)):
        item = col_model[col_index]
        assert isinstance(item, SalesItem)
        print('{}'.format(item.revenue),
              end='\t')
    print()

if __name__ == '__main__':
    unittest.main()
