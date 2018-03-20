from concurrent import futures

import time


class HourGlass(object):
    def __init__(self):
        self.arr = [[1, 1, 1, 0, 0, 0]
            , [0, 1, 0, 0, 0, 0]
            , [1, 1, 1, 0, 0, 0]
            , [0, 0, 2, 4, 4, 0]
            , [0, 0, 0, 2, 0, 0]
            , [0, 0, 1, 2, 4, 0]]

    def executor_multiple_hr(self):
        workers = 3
        list_coords = []
        max_value = 0
        for indx in range(1, 5):
            for jndx in range(1, 5):
                list_coords.append((indx, jndx))
        with futures.ProcessPoolExecutor(workers) as executor:
            another_generator = executor.map(self.executor_single_hr, list_coords)
            for gen_value in another_generator:
                max_value = max(max_value, gen_value)
        print(max_value)

    def executor_single_hr(self, coord):
        indx, jndx = coord
        a0 = self.nnw(indx, jndx)
        a1 = self.north(indx, jndx)
        a2 = self.nne(indx, jndx)
        a3 = self.west(indx, jndx)
        a4 = self.central(indx, jndx)
        a5 = self.east(indx, jndx)
        a6 = self.ssw(indx, jndx)
        a7 = self.south(indx, jndx)
        a8 = self.sse(indx, jndx)
        # syntax error -> yield a0 + ... + a8
        # executor.map() returns a generator
        # TypeError: can't pickle generator objects
        return a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

    def generator_multiple_hr(self):
        m1 = 0
        for m0 in self.generator_single_hr():
            m1 = max(m1, m0)
        print(m1)

    def generator_single_hr(self):
        for indx in range(1, 5):
            for jndx in range(1, 5):
                a0 = self.nnw(indx, jndx)
                a1 = self.north(indx, jndx)
                a2 = self.nne(indx, jndx)
                a3 = self.west(indx, jndx)
                a4 = self.central(indx, jndx)
                a5 = self.east(indx, jndx)
                a6 = self.ssw(indx, jndx)
                a7 = self.south(indx, jndx)
                a8 = self.sse(indx, jndx)
                yield a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

    def nnw(self, indx, jndx):
        row = indx - 1
        col = jndx - 1
        return self.arr[row][col]

    def north(self, indx, jndx):
        row = indx - 1
        col = jndx
        return self.arr[row][col]

    def nne(self, indx, jndx):
        row = indx - 1
        col = jndx + 1
        return self.arr[row][col]

    def west(self, indx, jndx):
        row = indx
        col = jndx - 1
        return self.arr[row][col]

    def central(self, indx, jndx):
        row = indx
        col = jndx
        return self.arr[row][col]

    def east(self, indx, jndx):
        row = indx
        col = jndx + 1
        return self.arr[row][col]

    def ssw(self, indx, jndx):
        row = indx + 1
        col = jndx - 1
        return self.arr[row][col]

    def south(self, indx, jndx):
        row = indx + 1
        col = jndx
        return self.arr[row][col]

    def sse(self, indx, jndx):
        row = indx + 1
        col = jndx + 1
        return self.arr[row][col]


if __name__ == '__main__':
    hg = HourGlass()
    t0 = time.time()
    hg.generator_multiple_hr()
    t1 = time.time()

    r0 = time.time()
    hg.executor_multiple_hr()
    r1 = time.time()

    print('Generator -> {}'.format(t1 - t0))
    print('Executor -> {}'.format(r1 - r0))

    # for i in range(1, len(arr) -1):
    # for j in range(1, len(arr[0]) - 1):
    # print('{} {} = {}'.format(i, j, arr[i][j]))

    # for i, j in zip(range(len(arr)), range(len(arr[0]))):
    # print('{} {} = {}'.format(i, j, arr[i][j]))
    """
        Results
        0 0 = 1
        1 1 = 1
        2 2 = 1
        3 3 = 4
        4 4 = 0
        5 5 = 0
        
        #!/bin/python3
        import sys
        
        arr = []
        for arr_i in range(6):
           arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
           arr.append(arr_t)
   """
