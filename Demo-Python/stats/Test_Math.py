import unittest

from itertools import product


class TestMath(unittest.TestCase):
    def test_iteration(self):
        self.assertEqual(True, True)

        for x in range(1, 9):
            print('x_value:div_mode = {}:{}'.format(x, x%2), end='\n')

        print()

        for y in range(1, 17):
            print('y_value:div_mode = {}:{}'.format(y, divmod(y, 4)),
                  end='\n')

    def test_product(self):
        num_items = 5
        num_decisions = 2 #ie, to be included or not to be included
        list_combinations = product(range(num_decisions), repeat=num_items)
        print(len(list(list_combinations)))

        list_combinations = product(range(num_decisions), repeat=num_items)
        for combination in list_combinations:
            print(combination)

if __name__ == '__main__':
    unittest.main()
