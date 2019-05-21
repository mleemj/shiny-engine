import unittest
from collections import deque

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


class SearchBfs(object):
    def bfs_search(self, graph: Graph, start: Node, dest: Node):
        # bfs_traverse to get parent
        parent = self.bfs_traverse(graph, start)
        path = self.child_to_parent_path(parent, child=dest)
        return path

    def child_to_parent_path(self, Parent: dict, child: Node, path=None):
        if path is None: path = list()
        path.append(child)
        parent = Parent.get(child)

        if parent is None: return path  # ie, start_node which is root

        return self.child_to_parent_path(Parent, child=parent, path=path)

    def bfs_traverse(self, graph: Graph, start: Node):
        Parent = dict()
        Parent[start] = None
        Queue = deque()
        Queue.append(start)

        while Queue:
            node = Queue.popleft()
            for child in graph.children_nodes(node.name):
                if child in Parent: continue
                Parent[child] = node
                Queue.append(child)
        return Parent


class SearchBfsTestCase(unittest.TestCase):
    def test_bfs_traverse(self):
        graph, cities = GraphBuilder().plot_graph()
        BFS = SearchBfs()
        path = BFS.bfs_traverse(graph, Node("Boston"))
        self.assertEqual(len(path), len(cities))

    def test_shortest_path(self):
        graph, cities = GraphBuilder().plot_graph()
        BFS = SearchBfs()
        path = BFS.bfs_search(graph, Node("Boston"), Node("Miami"))
        pretty_print(path)
