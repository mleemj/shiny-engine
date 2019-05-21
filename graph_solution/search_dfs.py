import unittest

from graph_solution.graph import Graph
from graph_solution.graph import GraphBuilder
from graph_solution.node import Node


def pretty_print(visited):
    print(len(visited))
    print('Path visited ', end=':')
    for v in visited:
        assert isinstance(v, Node)
        print(str(v.name), end=' ')
    print()


class SearchDfs(object):

    def recur_search(self, graph, start, dest):
        if not (graph.has_node(start.name) and graph.has_node(dest.name)): return None
        if start == dest: return [start]

        return self._search(graph, start, dest, steps=list())

    def _search(self, graph, start, dest, steps):
        steps.append(start)
        for node in graph.children_nodes(start.name):
            if node in steps: continue
            if dest in steps: return steps
            return self._search(graph, start=node, dest=dest, steps=steps)
        return None  # not found

    def recur_traverse(self, graph: Graph, start: Node, steps=None):
        if not graph.has_node(start.name):
            return None

        if steps is None: steps = list()
        steps.append(start)

        for node in graph.children_nodes(start.name):
            if node in steps: continue
            self.recur_traverse(graph, start=node, steps=steps)
        return steps


class SearchDfsTestCase(unittest.TestCase):
    def test_dfs_traverse(self):
        graph, list_of_cities = GraphBuilder().plot_graph()
        DFS = SearchDfs()
        Boston = Node("Boston")
        path = DFS.recur_traverse(graph, Boston)
        self.assertEqual(len(list_of_cities), len(path))

    def test_dfs_search(self):
        graph, list_of_cities = GraphBuilder().plot_graph()
        DFS = SearchDfs()
        Boston = Node("Boston")
        Miami = Node("Miami")
        path = DFS.recur_search(graph, Boston, Miami)
        self.assertEqual(len(path), 12)

    def test_dfs_not_conneted_node(self):
        graph, list_of_cities = GraphBuilder().plot_graph()
        Singapore = Node("Singapore")
        graph.add_node(Singapore.name)
        self.assertTrue(graph.has_node("Singapore"))

        DFS = SearchDfs()
        Boston = Node("Boston")
        path = DFS.recur_search(graph, Boston, Singapore)
        self.assertIsNone(path)
