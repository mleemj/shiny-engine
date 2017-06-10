from collections import namedtuple
from itertools import product
from typing import Type

from stats.Graph_View import PNode, PGraph, Coord

DataTuple = namedtuple("DataTuple", ('row_data', 'col_data'))


class StatsGraphMediator(object):
    def __init__(self, data_row: Type[list], data_col: Type[list]):
        assert isinstance(data_row, list)
        assert isinstance(data_col, list)
        self._row_model = data_row
        self._col_model = data_col

        self._data_map = None
        self._view_map = None

        self._graph = None
        self.build_empty_graph()

    @property
    def view_map(self):
        assert isinstance(self._view_map, dict)
        return self._view_map

    @property
    def graph(self):
        return self._graph

    # Build a unvisited graph
    def build_empty_graph(self):
        self._graph = PGraph()
        num_rows = len(self._row_model)
        num_cols = len(self._col_model)
        self._graph.num_rows = num_rows
        self._graph.num_cols = num_cols

        self.build_maps()

        graph_coords = self._view_map.values()

        for row_col_coord in graph_coords:
            row_index = row_col_coord[0]
            col_index = row_col_coord[1]
            pnode = PNode(row=row_index, col=col_index, has_visitor=False,
                          value=None)
            self._graph.add_node(pnode)
        return self._graph

    def build_data_tuple(self, row_col_product):
        for data_tuple in row_col_product:
            yield DataTuple(row_data=data_tuple[0], col_data=data_tuple[1])

    def build_graph_coord(self, graph_product):
        for coord in graph_product:
            yield Coord(row=coord[0], col=coord[1])

    def build_maps(self):
        assert isinstance(self._row_model, list)
        assert isinstance(self._col_model, list)

        # Graph is zero-based.
        num_rows_in_graph = range(len(self._row_model))
        num_cols_in_graph = range(len(self._col_model))

        list_rows_in_graph = list(num_rows_in_graph)
        list_cols_in_graph = list(num_cols_in_graph)

        view_product = product(list_rows_in_graph, list_cols_in_graph)
        list_view_coords = self.build_graph_coord(view_product)

        # data_model may not be zero based
        data_product = product(self._row_model, self._col_model)
        list_data_tuples = self.build_data_tuple(data_product)

        '''map(data_coord, view_coord)'''
        self._view_map = dict(zip(list_data_tuples, list_view_coords))

        '''map(view_coord, data_coord)'''
        self._data_map = self.invert_dict(self._view_map)

    def invert_dict(self, d):
        return dict([(v, k) for k, v in d.items()])

    def mark_nodes(self, data_model):
        assert isinstance(data_model, dict)
        list_data_rows = data_model.keys()

        node_generator = lambda data_row: self.generate_marked_nodes(
            data_row, data_model)

        generated_lists = map(node_generator, list_data_rows)

        for gen_node in generated_lists:
            try:
                list_marked_nodes = next(gen_node)  # May raise StopIteration
                assert isinstance(list_marked_nodes, list)
                for marked_node in list_marked_nodes:
                    assert isinstance(marked_node, PNode)
                    marked_node.set_visitor(has_visitor=True)
            except StopIteration:
                return  # One of the iterators has been exhausted

    def generate_marked_nodes(self, data_row, data_model):
        if data_row not in self._row_model:
            raise ValueError('Data row not found in rows model')

        list_marked_nodes = list()

        list_data_cols = data_model.get(data_row)

        for data_col in list_data_cols:
            if data_col not in self._col_model:
                raise ValueError('Data col not found in cols model')

            # Get the view co-ordinates from the data_view_model
            view_coord = self._view_map.get((data_row, data_col))

            if view_coord is None:
                raise ValueError('Data model not found in view model')

            node_with_value = self.graph.get_node(Coord(view_coord[0],
                                                     view_coord[1]))
            if node_with_value is None:
                raise ValueError('Co-ordinates not found in graph')

            assert isinstance(node_with_value, PNode)
            node_with_value.set_value(valueObject=DataTuple(row_data=data_row,
                                                         col_data=data_col))
            list_marked_nodes.append(node_with_value)

        yield list_marked_nodes

    def print_graph(self):
        assert isinstance(self.graph, PGraph)

        for row_index in range(len(self._row_model)):
            end_row = '\t\t\t\t'

            print('row = {}'.format(row_index), end=end_row)

            for col_index in range(len(self._col_model)):
                coord = Coord(row=row_index, col=col_index)
                node = self.graph.get_node(coord)
                assert isinstance(node, PNode)
                if node.value is not None:
                    print(1, end='\t')
                else:
                    print(0, end='\t')
            print('row_data = {}'.format(self._row_model[row_index]))

        print('\ncol = ', end='\t\t\t\t')
        for col_index in range(len(self._col_model)):
            print('{}'.format(col_index), end='\t')

        print('\ncol_data = ', end='\t\t\t')
        for col_index in range(len(self._col_model)):
            print('{}'.format(self._col_model[col_index]),
                  end='\t')

        print('\n')
