import unittest

from itertools import product

from collections import deque


class TestHelpers(unittest.TestCase):
    def test_append(self):
        print('test_append')
        self.assertTrue(True)
        list_something = list()
        # Will not work -> list_something.append()
        print(list_something)

    def test_enumerate_product(self):
        self.assertEqual(True, True)
        a = [10, 11, 12, 13, 14]
        b = [10, 11, 12, 13, 14]
        cartesian_product = product(a, b)

        print('test_enumerate_product')
        enumerate_product = enumerate(cartesian_product)
        for count, productTuple in enumerate_product:
            self.assertIsInstance(productTuple, tuple)
            print('index:row:col = {index}:{row}:{col}'
                  .format(index=count,
                          row=productTuple[0],
                          col=productTuple[1]))
            print()

        cartesian_product = product(a, b)

        for cp_tuple in cartesian_product:
            print('{}:{}'.format(cp_tuple[0], cp_tuple[1]), end='\t')

    def test_map(self):
        print('test_map')
        # list(map(lambda x: x ** 2, range(10)))
        self.assertEqual(True, True)
        row = list([10, 11, 12, 13, 14])
        col = list([100, 110, 120, 130, 140, 150, 160])
        cartesian_product_data = product(row, col)
        view_row = list(range(len(row)))
        view_col = list(range(len(col)))
        print(view_row)
        print(view_col)
        cartesian_product_view = product(view_row, view_col)
        print('map product tuple')
        self.generate_coord(cartesian_product_view, row, col)
        self.generate_view_data_model(cartesian_product_data,
                                      cartesian_product_view)

    def test_more_map(self):
        print()
        print('test_more_map')
        # list(map(lambda x: x ** 2, range(10)))
        self.assertEqual(True, True)
        row = list([10, 11, 12, 13, 14])
        col = list([100, 110, 120, 130, 140, 150, 160])
        cartesian_product_data = product(row, col)
        view_row = list(range(len(row)))
        view_col = list(range(len(col)))
        cartesian_product_view = product(view_row, view_col)
        self.generate_view_data_model(cartesian_product_data,
                                      cartesian_product_view)

    def generate_view_data_model(self, data_product, view_product):
        data_dict = dict(zip(data_product, view_product))
        print('test_generate_view_data_model')
        for data_key in data_dict.keys():
            print('data_key = {}:{}'.format(data_key[0], data_key[1]))
            view_tuple = data_dict[data_key]
            print('view_coords = {}:{}'.format(view_tuple[0], view_tuple[1]))
            print()

    def generate_coord(self, cart_product, row_model, col_model):
        for cartesian_tuple in cart_product:
            row_index = cartesian_tuple[0]
            col_index = cartesian_tuple[1]
            print('view_row:view_col = {}:{}'.format(row_index, col_index))
            row_data = row_model[row_index]
            col_data = col_model[col_index]
            print('row_data:col_data = {}:{}'.format(row_data, col_data))
            print()

    def test_deque(self):
        print('test deque')
        cq = deque()
        cq.append(1)
        cq.append(2)
        cq.append(3)
        while(cq):
            print('{}'.format(cq.popleft()), end=' , ')
        print()

    def test_stack(self):
        print('test stack')
        cs = list()
        cs.append(1)
        cs.append(2)
        cs.append(3)
        while (cs):
            print('{}'.format(cs.pop()), end=' , ')
        print()


if __name__ == '__main__':
    unittest.main()
