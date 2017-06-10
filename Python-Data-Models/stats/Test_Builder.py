import unittest

from numpy import random as npr, arange

from stats.Graph_View import PNode, PGraph, Coord
from stats.Stats import T2DmGroup, PCounter, \
    Glucose_HDL_GroupStrategy
from stats.Stats_Graph_Mediator import StatsGraphMediator, DataTuple


class TestBuilder(unittest.TestCase):
    def setUp(self):
        # numpy arange includes start and stop values
        self.col_model = list(arange(41, 61, 1))
        self.row_model = list()
        for r in range(41, 71, 1):
            float_value = round(r / 10 * 1.0, 1)
            self.row_model.append(float_value)
        self.map_decimals = map(lambda fnum: round(fnum, 1), self.row_model)

        self.data_group = T2DmGroup()
        patient_id = PCounter()

        for i in range(100):
            Ldl = npr.randint(low=101, high=160)
            Hdl = npr.randint(low=41, high=60)
            A1c = round(npr.uniform(4.1, 7.0), 1)
            self.data_group.add_participant(pid=patient_id(), glucose=A1c,
                                            hdl=Hdl, ldl=Ldl)

        self.data_model = self.data_group.groupBy(Glucose_HDL_GroupStrategy())

    def test_build_graph(self):
        self.assertTrue(True)
        self.assertIsInstance(self.data_model, dict)
        print(len(self.row_model))
        for row in self.row_model:
            print(row, end='\t')

        print()
        print(len(self.col_model))
        for col in self.col_model:
            print(col, end='\t')

        print()
        for row_stat in self.data_model.keys():
            print(row_stat)
            col_stats = self.data_model.get(row_stat)
            print(col_stats)

        print()
        for d in self.map_decimals:
            print(d, sep=',')

    def test_mediator(self):
        mediator = StatsGraphMediator(self.row_model, self.col_model)

        mediator.mark_nodes(self.data_model)

        graph = mediator.graph
        self.assertIsInstance(graph, PGraph)

        list_visited_nodes = list()
        for node in graph.nodes:
            self.assertIsInstance(node, PNode)
            if node.value is not None:
                list_visited_nodes.append(node)


        print('test_mediator list_visited_nodes')
        for node in list_visited_nodes:
            self.assertIsInstance(node, PNode)
            if node.has_visitor:
                print('view_model:', end='\t')
                print('row:col:node_has_visitor = {row}:{col}:{visited}'
                      .format(row=node.coord.row,
                              col=node.coord.col,
                              visited=node.has_visitor))

        graph = mediator.graph
        self.assertIsInstance(graph, PGraph)

        self.assertIsInstance(self.data_model, dict)

        for r_key in self.data_model.keys():
            c_list = self.data_model.get(r_key)

            for c_key in c_list:
                view_map = mediator.view_map
                self.assertIsInstance(view_map, dict)
                coord = view_map.get(DataTuple(r_key, c_key))
                self.assertIsInstance(coord, Coord)
                pnode = graph.get_node(coord)

                self.assertIsInstance(pnode, PNode)
                print('ROW:COL:HAS_VISTOR = {prow}:{pcol}:{pvisitor}'.format(
                    prow=coord.row, pcol=coord.col,
                    pvisitor=pnode.has_visitor))
                print()

                test_data_tuple = pnode.value
                self.assertIsNotNone(test_data_tuple)
                self.assertIsInstance(test_data_tuple, DataTuple)

                if test_data_tuple is not None:
                    self.assertEqual(r_key, test_data_tuple.row_data)
                    self.assertEqual(c_key, test_data_tuple.col_data)

                    print('Control data model : Model from PGraph')
                    print('{data_row}:{data_col} = {test_data_row}:{'
                          'test_data_col}'.format(
                        data_row=r_key,
                        data_col=c_key,
                        test_data_row=test_data_tuple.row_data,
                        test_data_col=test_data_tuple.col_data))
        mediator.print_graph()

if __name__ == '__main__':
    unittest.main()
