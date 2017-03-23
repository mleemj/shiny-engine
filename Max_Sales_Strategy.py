from stats.Graph_View import PGraph, PNode

from itertools import product

class MaxSalesStrategy(object):
    def __init__(self, num_items):
        self.num_of_items = num_items

    def get_list_combinations(self):
        # One means item is included in the combination
        # Zer0 means item is not included in the combination
        list_combinations = product(range(2), repeat=self.num_of_items)
        return list_combinations


