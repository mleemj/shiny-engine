import unittest


def selection_sort(items):
    for indx in range(len(items)):
        temp_indx = indx

        for in_indx in range(indx + 1, len(items)):
            if items[in_indx] < items[temp_indx]:
                temp_indx = in_indx

        if temp_indx != indx:
            temp = items[indx]
            items[indx] = items[temp_indx]
            items[temp_indx] = temp


class SelectionSortTestCase(unittest.TestCase):
    def test_something(self):
        items = [2, 6, 3, 1]
        selection_sort(items=items)
        self.assertEqual(items, [1, 2, 3, 6])


if __name__ == '__main__':
    unittest.main()
