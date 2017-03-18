import unittest
from unittest import TestCase

from numpy import random as npr, ndarray, nditer, empty, arange, round

from stats.Graph_View import PGraph, PNode, Coord
from stats.Stats import PCounter
from stats.Stats import T2DmGroup, Glucose_HDL_GroupStrategy


class TestDmSearch(TestCase):
    def test_glucose_hdl(self):
        patient_group = T2DmGroup()
        patient_id = PCounter()

        for i in range(100):
            Hdl = npr.randint(low=40, high=60)
            Ldl = npr.randint(low=100, high=190)
            A1c = '{:.1f}'.format(npr.uniform(4.0, 7.1))
            patient_group.add_participant(pid=patient_id(), glucose=A1c,
                                          hdl=Hdl, ldl=Ldl)

        a1c_hdl_dict = patient_group.groupBy(Glucose_HDL_GroupStrategy())
        self.assertIsInstance(a1c_hdl_dict, dict)
        print('test_glucose_hdl')
        for a1c_key in a1c_hdl_dict.keys():
            print('glucose:hdl = {glucose}:{hdl}'
                  .format(glucose=a1c_key, hdl=a1c_hdl_dict[a1c_key]))
            print()

        hdl_array = arange(start=40, stop=61, step=1)
        hdl_list = hdl_array.tolist()
        a1c_array = round(arange(start=4.0, stop=7.1, step=0.1), decimals=1)
        print('test_glucose_hdl')
        print(hdl_array)
        print(a1c_array)

        for index in range(21):
            hdl = hdl_array[index]
            print('index:hdl = {idx}:{hdl_value}'
                  .format(idx=index, hdl_value=hdl))
            print('from hdl_list = {}'.format(hdl_list.index(hdl)))

        for aIndx in range(31):
            print('index:A1c = {idx}:{a1c}'.format(idx=aIndx,
                                                   a1c=a1c_array[aIndx]))

    def test_sample_file(self):
        self.assertTrue(True)
        test_file = open('../resources/sample_data.txt', 'r')
        test_str = test_file.readline()
        data = list()
        while len(test_str) != 0:
            data.append(test_str.strip().split())
            test_str = test_file.readline()

        for d in data:
            print(d)
        # close file io
        test_file.close()

    def test_dfs_search(self):
        print('test_dfs_search')
        self.assertEqual(True, True)

    def test_build_graph(self):
        print('test_build_graph')
        test_p_graph = PGraph()

        num_rows = 60 - 40
        num_cols = int((7 - 4) / 0.1)
        sample_array = empty([num_rows, num_cols], dtype=int)
        self.assertIsInstance(sample_array, ndarray)
        sample_iter = nditer(sample_array, flags=['multi_index'])

        while not sample_iter.finished:
            row_index = sample_iter.multi_index[0]
            col_index = sample_iter.multi_index[1]

            random_visitor = npr.randint(0, 1)
            has_random_visitor = True if random_visitor == 1 else False

            control_node = PNode(row=row_index, col=col_index,
                                 has_visitor=has_random_visitor)

            if random_visitor == 1:
                self.assertTrue(control_node.has_visitor)
            else:
                self.assertFalse(control_node.has_visitor)

            test_p_graph.add_node(control_node)

            print("Control data:\trow : col : has_visitor")
            control_data_str = "control_data:\t{row} : {col}" \
                               ": {has_visitor}" \
                .format(row=row_index, col=col_index,
                        has_visitor=has_random_visitor)

            test_data = test_p_graph.get_node(coord=Coord(row=row_index,
                                                          col=col_index))
            self.assertIsInstance(test_data, PNode)
            self.assertIsNotNone(test_p_graph.has_node(node=test_data))

            test_row = test_data.coord.row
            test_col = test_data.coord.col
            test_visitor = test_data.has_visitor

            self.assertEqual(row_index, test_row)
            self.assertEqual(col_index, test_col)
            self.assertEqual(has_random_visitor, test_visitor)

            test_data_str = "test_node_d:\t{row} : {col}" \
                            ": {has_visitor}".format(row=test_row,
                                                     col=test_col,
                                                     has_visitor=test_visitor)
            print(control_data_str)
            print(test_data_str)
            print()
            sample_iter.iternext()

    def test_node(self):
        print('test_node')
        node_control = PNode(row=1, col=1)
        node_test = PNode(row=1, col=1, has_visitor=True, value=1)
        self.assertEqual(node_control, node_test)
        self.assertNotEqual(node_control.value, node_test.value)

    def test_TypeError(self):
        pnode = PNode(None, None, None, None)
        self.assertFalse(pnode.check_is_node_valid(other=None))


if __name__ == '__main__':
    unittest.main()
