from collections import deque, namedtuple
from typing import Type

Coord = namedtuple('Coord', ('row', 'col'))


class PNode(object):
    def __init__(self, row, col, has_visitor=None, value=None):
        self._coord = Coord(row, col)
        self._value = value
        self._visited = has_visitor

    @property
    def coord(self):
        return self._coord

    @property
    def has_visitor(self):
        return self._visited

    # value of the node
    @property
    def value(self):
        return self._value

    def set_visitor(self, has_visitor: Type[bool]):
        self._visited = has_visitor

    def set_value(self, valueObject):
        self._value = valueObject

    # Private helper method to check if other is also a duck
    def check_is_node_valid(self, other):
        is_valid = hasattr(other, 'coord') and hasattr(other, 'value') and \
                   hasattr(other, 'has_visitor')
        return is_valid

    def __hash__(self):
        odd_hash_value = int(((self.coord.row + self.coord.col) * 2) + 1)
        return odd_hash_value

    def __eq__(self, other):
        node_is_valid = self.check_is_node_valid(other)
        if not node_is_valid:
            return False

        node_is_equal = (other.coord.row == self.coord.row) and \
                        (other.coord.col == self.coord.col)
        return node_is_equal


class PGraph(object):
    def __init__(self):
        self._nodes = None
        self._children = None
        self._num_rows = 0
        self._num_cols = 0

    @property
    def num_rows(self):
        return self._num_rows

    @num_rows.setter
    def num_rows(self, nrow):
        self._num_rows = nrow

    @property
    def num_cols(self):
        return self._num_cols

    @num_cols.setter
    def num_cols(self, ncol):
        self._num_cols = ncol

    def childrenOf(self, src_node):
        assert isinstance(src_node, PNode)
        assert isinstance(self._children, dict)
        return self._children.get(src_node)

    @property
    def nodes(self):
        assert isinstance(self._nodes, dict)
        return list(self._nodes.values())

    def has_node(self, node):
        assert isinstance(node, PNode)
        return self._nodes.get(node.coord)

    def get_node(self, coord):
        assert isinstance(coord, Coord)
        assert isinstance(self._nodes, dict)
        return self._nodes.get(coord)

    def add_node(self, node: Type[PNode]):
        if self._nodes is None:
            self._nodes = dict()
            self._children = dict()
        assert isinstance(node, PNode)
        coord = node.coord
        self._nodes[coord] = node
        self._children[node] = list()

    def _add_edge(self, src_node, dest_node):
        assert isinstance(src_node, PNode)
        assert isinstance(dest_node, PNode)
        dest_list = self._children.get(src_node)

        assert isinstance(dest_list, list)
        if dest_node not in dest_list:
            dest_list.append(dest_node)

    def add_edge(self, edge):
        assert isinstance(edge, PEdge)
        self._add_edge(edge.src_node, edge.dest_node)
        # Add reverse direction
        self._add_edge(edge.dest_node, edge.src_node)


class PEdge(object):
    def __init__(self, src_node, dest_node):
        assert isinstance(src_node, PNode)
        assert isinstance(dest_node, PNode)
        self._src_node = src_node
        self._dest_node = dest_node

    @property
    def src_node(self):
        return self._src_node

    @property
    def dest_node(self):
        return self._dest_node


class SimpleSearcher(object):
    def __init__(self, graph):
        self.graph = graph

    def search_by_row(self, row_index):
        num_cols = self.graph.num_cols
        list_cols = list()
        for c in range(num_cols):
            node = self.graph.get_node(Coord(row_index, c))
            assert isinstance(node, PNode)
            if node.value is not None:
                list_cols.append(c)
        return list_cols


class PSearcher(object):
    def __init__(self, graph):
        self.graph = graph

    def add_edges(self):
        generated_src_node = self.generate_src_node(self.graph.nodes)

        edge_list_generator = lambda src_node: self.generate_edge_list(
            src_node)

        generated_edge_list = map(edge_list_generator, generated_src_node)

        for edge_list in generated_edge_list:
            try:
                for edge in edge_list:
                    assert isinstance(self.graph, PGraph)
                    self.graph.add_edge(edge)
            except StopIteration:
                return

    def generate_src_node(self, nodes_in_graph):
        for node in nodes_in_graph:
            assert isinstance(node, PNode)
            if node.has_visitor:
                yield node

    def generate_edge_list(self, src_node):
        assert isinstance(src_node, PNode)
        src_row = src_node.coord.row
        src_col = src_node.coord.col

        """ if src_row is top most row, then top_row = -1
            if src_row is last row, then bottom_row = -1"""
        top_row = src_row - 1 if src_row > 0 else -1
        bottom_row = src_row + 1 if src_row < self.graph.num_rows - 1 else -1

        left_col = src_col - 1 if src_col > 0 else -1
        right_col = src_col + 1 if src_col < self.graph.num_cols - 1 else -1

        list_of_edges = list()

        edge_accumulator = \
            lambda src_dest_edge: self.accumulate_edge_to_list(src_dest_edge,
                                                               list_of_edges)

        single_edge_generator = lambda row, col: self.generate_edge(
            Coord(row, col),
            src_node.coord)

        top_left = single_edge_generator(top_row, left_col)
        edge_accumulator(top_left)

        top_center = single_edge_generator(top_row, src_col)
        edge_accumulator(top_center)

        top_right = single_edge_generator(top_row, right_col)
        edge_accumulator(top_right)

        left_node = single_edge_generator(src_row, left_col)
        edge_accumulator(left_node)

        right_node = single_edge_generator(src_row, right_col)
        edge_accumulator(right_node)

        bottom_left = single_edge_generator(bottom_row, left_col)
        edge_accumulator(bottom_left)

        bottom_center = single_edge_generator(bottom_row, src_col)
        edge_accumulator(bottom_center)

        bottom_right = single_edge_generator(bottom_row, right_col)
        edge_accumulator(bottom_right)

        return list_of_edges

    def accumulate_edge_to_list(self, edge, edge_list):
        if edge is not None:
            edge_list.append(edge)

    def generate_edge(self, dest_coord, src_coord):
        assert isinstance(src_coord, Coord)
        src_node = self.graph.get_node(src_coord)
        assert isinstance(src_node, PNode)
        if src_node.value is None:
            return None

        assert isinstance(dest_coord, Coord)
        row = dest_coord.row
        col = dest_coord.col

        if row != -1 and col != -1:
            dest_node = self.graph.get_node(dest_coord)
            assert isinstance(dest_node, PNode)
            if dest_node.value is not None:
                return PEdge(src_node, dest_node)

        return None  # Return None

    def dfs_search(self, start_node, list_connected_nodes=None):
        if list_connected_nodes is None:
            list_connected_nodes = list()
        else:
            assert isinstance(list_connected_nodes, list)

        assert isinstance(start_node, PNode)
        if start_node.value is None:
            return list_connected_nodes

        list_connected_nodes.append(start_node)

        children_of_start_node = self.graph.childrenOf(start_node)
        for child in children_of_start_node:
            if child not in list_connected_nodes:
                list_connected_nodes = \
                    self.dfs_search(child, list_connected_nodes)

        return list_connected_nodes

    def bfs_search(self, start_node, graph):
        self.reset_nodes(graph)
        assert isinstance(start_node, PNode)
        if start_node.value is None:
            return None
        unvisited_nodes = deque()
        unvisited_nodes.append(start_node)

        while (unvisited_nodes):
            visited_node = unvisited_nodes.popleft()
            assert isinstance(visited_node, PNode)
            if visited_node.has_visitor is True:
                continue

            visited_node.set_visitor(has_visitor=True)

            visit_children = graph.childrenOf(visited_node)

            for child_node in visit_children:
                assert isinstance(child_node, PNode)
                if child_node.value is not None \
                        and child_node.has_visitor is False:
                    unvisited_nodes.append(child_node)
            yield visited_node

        self.reset_nodes(graph)

    def reset_nodes(self, graph):
        assert isinstance(graph, PGraph)
        list_nodes = graph.nodes
        for node in list_nodes:
            assert isinstance(node, PNode)
            node.set_visitor(has_visitor=False)
