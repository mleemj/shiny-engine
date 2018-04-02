import sys

from collections import deque

class Libroad(object):
    def __init__(self):
        self.dict_node = dict()

    def build_graph(self, num_citi, citi_conex):
        for indx in range(1, num_citi + 1):
            self.dict_node[indx] = set([])

        for conex in citi_conex:
            c1, c2 = conex[0], conex[1]
            s1 = self.dict_node[c1]
            s2 = self.dict_node[c2]
            s1.add(c2)
            s2.add(c1)
        print(self.dict_node)

    # Complete this function
    def roadsAndLibraries(self, num_citi, cost_lib, cost_road, citi_conex):
        s1 = set({1, 2, 3})
        s2 = set({3, 2})
        print(s1 == s2)
        print(s1.issubset(s2))
        print(s1.difference(s2))
        self.build_graph(num_citi, citi_conex)
        queue = deque()
        queue.append(1)
        self.rec_dfs(set_visited=None, queue=queue)

    def rec_dfs(self, set_visited, queue):
        if set_visited is None: set_visited = set()
        assert isinstance(queue, deque)
        node_id = queue.popleft()
        print('rec_dfs {}'.format(node_id))
        set_visited.add(node_id)

        while len(queue) > 0:
            set_neighbr = self.dict_node(node_id)
            for neighbr in set_neighbr:
                if neighbr not in set_visited:
                    queue.append(neighbr)
            self.rec_dfs(set_visited, queue)

    def add_list_to_dict(self):
        list_path = dict()
        s1 = list()
        s1.append(1)
        s1.append(2)
        s1.append(3)
        s1.append(4)
        list_path[0] = s1
        print(list_path)
        s2 = list()
        s2.append(5)
        s2.append(6)
        list_path[1] = s2
        print(list_path)


    def read_input(self):
        q = int(input().strip())
        for a0 in range(q):
            n, m, c_lib, c_road = input().strip().split(' ')
            n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
            cities = []
            for cities_i in range(m):
                cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
                cities.append(cities_t)


if __name__ == "__main__":
    lr = Libroad()
    num_citi = 3
    citi_conex = [[1, 2], [3, 1], [2, 3]]
    result = lr.roadsAndLibraries(num_citi, 2, 1, citi_conex)

    #print(result) # expected answer is 4
    #result = lr.roadsAndLibraries(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]])
    #print(result) # expected answer is 12

        # Sample
        # Input
        #
        # 2
        # 3 3 2 1
        # 1 2
        # 3 1
        # 2 3
        # 6 6 2 5
        # 1 3
        # 3 4
        # 2 4
        # 1 2
        # 2 3
        # 5 6

        #Answer
        # 4 12