import random
import unittest

from numpy import random as npr, arange

from stats.Stats import T2DmGroup, PCounter, \
    Glucose_HDL_GroupStrategy
from stats.Stats_Graph_Mediator import StatsGraphMediator
from stats.Graph_View import PGraph, PNode


class TestMediator(unittest.TestCase):
    def test_mediator(self):
        patient_group = T2DmGroup()
        patient_id = PCounter()

        for i in range(100):
            Hdl = npr.randint(low=40, high=60)
            Ldl = npr.randint(low=100, high=190)
            A1c = '{:.1f}'.format(random.uniform(4.0, 7.0))
            patient_group.add_participant(pid=patient_id(), glucose=A1c,
                                          hdl=Hdl, ldl=Ldl)

        t2DmDict = patient_group.groupBy(Glucose_HDL_GroupStrategy())
        self.assertIsInstance(t2DmDict, dict)
        for a1cKey in t2DmDict.keys():
            hdl_set = t2DmDict[a1cKey]
            for hdl_data in hdl_set:
                self.assertIsNotNone(hdl_data)

    def test_build_graph(self):
        cols_in_graph = arange(start=40, stop=61, step=1).round(
            decimals=1).tolist()
        rows_in_graph = arange(start=4.0, stop=7.1, step=0.1).round(
            decimals=1).tolist()

        mediator = StatsGraphMediator(rows_in_graph, cols_in_graph)

        patient_group = T2DmGroup()
        patient_id = PCounter()

        for i in range(100):
            Hdl = npr.randint(low=40, high=60)
            Ldl = npr.randint(low=100, high=190)
            A1c = '{:.1f}'.format(random.uniform(4.0, 7.0))
            patient_group.add_participant(pid=patient_id(), glucose=A1c,
                                          hdl=Hdl, ldl=Ldl)

        t2DmDict = patient_group.groupBy(Glucose_HDL_GroupStrategy())

        mediator.mark_visited_nodes(t2DmDict)

        graph = mediator.graph
        self.assertIsInstance(graph, PGraph)
        list_nodes = graph.nodes
        list_visited_nodes = list()

        for node in list_nodes:
            self.assertIsInstance(node, PNode)
            if node.has_visitor:
                list_visited_nodes.append(node)

        mediator.print_graph()

        for visitor in list_visited_nodes:
            node = visitor
            node_has_visitor = node.has_visitor
            coord = node.coord
            row_index = coord.row
            col_index = coord.col
            self.assertTrue(node_has_visitor)

            print(
                'row : col : node_has_visitor = {row} : {col}'
                ':{node_has_visitor}'.format(
                    row=row_index,
                    col=col_index,
                    node_has_visitor=node_has_visitor))

        mediator.print_graph()


if __name__ == '__main__':
    unittest.main()
