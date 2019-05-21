import unittest

from graph_solution.node import Node


class Graph(object):
    def __init__(self):
        self._nodes = dict()
        self._edges = dict()

    def __str__(self):
        result = ''
        for src in self._nodes:
            result = result + src.name + ' -> ' + f"{self.children_nodes(src)}" + '\n'
        return result

    def has_node(self, node_name):
        return node_name in self._nodes.keys()

    @property
    def nodes(self):
        return self._nodes

    def get_node(self, node_name):
        return self._nodes.get(node_name)

    def add_node(self, node_name):
        if node_name in self._nodes.keys():
            return
        node = Node(node_name)
        self._nodes[node_name] = node
        self._edges[node_name] = list()

    def add_edge(self, start_name, dest_name):
        if not (start_name in self._nodes.keys() and dest_name in self._nodes.keys()):
            raise ValueError
        start = self._nodes.get(start_name)
        dest = self._nodes.get(dest_name)
        self._add_edge(start=start, dest=dest)
        self._add_edge(start=dest, dest=start)

    def _add_edge(self, start: Node, dest: Node):
        self._edges[start.name].append(dest)

    def children_nodes(self, node_name):
        return self._edges.get(node_name)


class GraphBuilder(object):

    def plot_graph(self):
        graph = Graph()
        list_cities = ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                       "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"]

        for citi in list_cities:
            graph.add_node(citi)

        graph.add_edge("Seattle", "Chicago")
        graph.add_edge("Seattle", "San Francisco")
        graph.add_edge("San Francisco", "Riverside")
        graph.add_edge("San Francisco", "Los Angeles")
        graph.add_edge("Los Angeles", "Riverside")
        graph.add_edge("Los Angeles", "Phoenix")
        graph.add_edge("Riverside", "Phoenix")
        graph.add_edge("Riverside", "Chicago")
        graph.add_edge("Phoenix", "Dallas")
        graph.add_edge("Phoenix", "Houston")
        graph.add_edge("Dallas", "Chicago")
        graph.add_edge("Dallas", "Atlanta")
        graph.add_edge("Dallas", "Houston")
        graph.add_edge("Houston", "Atlanta")
        graph.add_edge("Houston", "Miami")
        graph.add_edge("Atlanta", "Chicago")
        graph.add_edge("Atlanta", "Washington")
        graph.add_edge("Atlanta", "Miami")
        graph.add_edge("Miami", "Washington")
        graph.add_edge("Chicago", "Detroit")
        graph.add_edge("Detroit", "Boston")
        graph.add_edge("Detroit", "Washington")
        graph.add_edge("Detroit", "New York")
        graph.add_edge("Boston", "New York")
        graph.add_edge("New York", "Philadelphia")
        graph.add_edge("Philadelphia", "Washington")

        return graph, list_cities


class GraphTestCase(unittest.TestCase):
    def test_add_node(self):
        city_graph, list_cities = GraphBuilder().plot_graph()
        for citi in list_cities:
            city_graph.add_node(citi)
        self.assertEqual(len(city_graph.nodes), len(list_cities))

    def test_has_node(self):
        city_graph, list_cities = GraphBuilder().plot_graph()
        for citi in list_cities:
            self.assertTrue(city_graph.has_node(citi))

    def test_get_children_nodes(self):
        city_graph, list_cities = GraphBuilder().plot_graph()
        chicago = [Node("Seattle"), Node("Riverside"), Node("Dallas"), Node("Atlanta"), Node("Detroit")]

        for node in city_graph.children_nodes("Chicago"):
            if node.name == "Seattle":
                self.assertEqual(node, Node("Seattle"))
            elif node.name == "Riverside":
                self.assertEqual(node, Node("Riverside"))
            elif node.name == "Dallas":
                self.assertEqual(node, Node("Dallas"))
            elif node.name == "Atlanta":
                self.assertEqual(node, Node("Atlanta"))
            elif node.name == "Detroit":
                self.assertEqual(node, Node("Detroit"))

    def test_seattle(self):
        city_graph, _ = GraphBuilder().plot_graph()
        seattle = ["Chicago", "San Francisco"]

        for child in city_graph.children_nodes("Seattle"):
            self.assertIn(str(child.name), seattle)