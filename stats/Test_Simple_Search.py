import random
import time
import unittest
from concurrent.futures import ProcessPoolExecutor
from itertools import product

from stats.Graph_View import PGraph, SimpleSearcher
from stats.Stats_Graph_Mediator import StatsGraphMediator


class TestSimpleSearch(unittest.TestCase):
    def test_transport_costs(self):
        start = time.time()
        for r_index in range(len(self.rows_data)):
            transport_cost_generator = self.simple_searcher.search_by_row(
                row_index
                =r_index)
            total_cost = 0
            for transport in transport_cost_generator:
                transport_cost = self.transport_cost_map.get(transport)
                total_cost += transport_cost

        end = time.time()
        duration = format(end - start, '.5f')
        print('Took {} for {} rows'.format(duration, len(self.rows_data)))
        self.assertEqual(True, True)

    def test_search_transport_cost(self):
        r_index = random.randint(1, len(self.rows_data) + 1)

        transport_cost_generator = self.simple_searcher.search_by_row(
            row_index
            =r_index)
        total_cost = 0
        for transport in transport_cost_generator:
            transport_cost = self.transport_cost_map.get(transport)
            total_cost += transport_cost

    def setUp(self):
        num_of_items = 10

        self.transport_cost_map = dict()

        for i in range(num_of_items):
            self.transport_cost_map[i] = random.randint(1, 10)

        list_combinations = product(range(2), repeat=num_of_items)

        num_of_rows = pow(2, num_of_items)

        self.rows_data = list(range(num_of_rows))
        self.cols_data = list(range(num_of_items))

        mediator = StatsGraphMediator(data_row=self.rows_data,
                                      data_col=self.cols_data)

        data_model = dict()

        row_index = 0
        for combination in list_combinations:
            col_index = 0
            list_items = list()
            for item in combination:
                if item is 1:
                    list_items.append(col_index)
                col_index += 1

            if len(list_items) > 0:
                data_model[row_index] = list_items
            row_index += 1

        mediator.mark_nodes(data_model)

        graph = mediator.graph

        self.assertIsInstance(graph, PGraph)
        self.simple_searcher = SimpleSearcher(graph)


if __name__ == '__main__':
    unittest.main()
