import unittest

from collections import deque


def rec_dfs(G, s, S=None):
    if S is None: S = list()  # Initialize the history
    S.append(s)  # We've visited s
    for u in G[s]:  # Explore neighbors
        if u in S:
            # print('Visited {}', S)
            continue  # Already visited: Skip
        rec_dfs(G, u, S)  # New: Explore recursively
    return S


def bfs(G, s):
    P, Q = {s: None}, deque([s])  # Parents and FIFO queue
    while Q:
        u = Q.popleft()  # Constant-time for deque
        for v in G[u]:
            if v in P: continue  # Already has parent
            P[v] = u  # Reached from u: u is parent
            Q.append(v)
    return P


# traverse graph, starting at root
def breath_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adjacent_nodes = graph[node]

        remaining_elements = set(adjacent_nodes).difference(set(visited_vertices))

        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)

    return visited_vertices


def iter_dfs(G, s):
    S, Q = set(), []  # Visited-set and queue
    Q.append(s)  # We plan on visiting s
    while Q:  # Planned nodes left?
        u = Q.pop()  # Get one
        if u in S: continue  # Already visited? Skip it
        S.add(u)  # We've visited it now
        Q.extend(G[u])  # Schedule all neighbors
        yield u  # Report u as visited


'''
Visited {} ['A', 'B']
Visited {} ['A', 'B', 'F']
Visited {} ['A', 'B', 'F', 'D']
Visited {} ['A', 'B', 'F', 'D']
Visited {} ['A', 'B', 'F', 'D', 'C']
Visited {} ['A', 'B', 'F', 'D', 'C', 'H']
Visited {} ['A', 'B', 'F', 'D', 'C', 'H', 'E']
Visited {} ['A', 'B', 'F', 'D', 'C', 'H', 'E', 'G']
Visited {} ['A', 'B', 'F', 'D', 'C', 'H', 'E', 'G']
Visited {} ['A', 'B', 'F', 'D', 'C', 'H', 'E', 'G']
Visited {} ['A', 'B', 'F', 'D', 'C', 'H', 'E', 'G']
'''


class MasterAlgorithm(unittest.TestCase):
    def test_recursive_dfs(self):
        graph = dict()
        graph['A'] = ['B', 'G', 'D']
        graph['B'] = ['A', 'F', 'E']
        graph['C'] = ['F', 'H']
        graph['D'] = ['F', 'A']
        graph['E'] = ['B', 'G']
        graph['F'] = ['B', 'D', 'C']
        graph['G'] = ['A', 'E']
        graph['H'] = ['C']
        result = rec_dfs(graph, 'A')
        # ['A', 'B', 'F', 'D', 'C', 'H', 'E', 'G']

    def test_iter_dfs(self):
        graph = dict()
        graph['A'] = ['B', 'G', 'D']
        graph['B'] = ['A', 'F', 'E']
        graph['C'] = ['F', 'H']
        graph['D'] = ['F', 'A']
        graph['E'] = ['B', 'G']
        graph['F'] = ['B', 'D', 'C']
        graph['G'] = ['A', 'E']
        graph['H'] = ['C']
        print('Iter DFS', end=' : ')
        # for n in iter_dfs(G=graph, s='A'):
        # print(n, end=', ')

    def test_breath_first_search(self):
        graph = dict()
        graph['A'] = ['B', 'G', 'D']
        graph['B'] = ['A', 'F', 'E']
        graph['C'] = ['F', 'H']
        graph['D'] = ['F', 'A']
        graph['E'] = ['B', 'G']
        graph['F'] = ['B', 'D', 'C']
        graph['G'] = ['A', 'E']
        graph['H'] = ['C']
        result = breath_first_search(graph, 'A')
        print(result)

    def test_bfs(self):
        graph = dict()
        graph['A'] = ['B', 'G', 'D']
        graph['B'] = ['A', 'F', 'E']
        graph['C'] = ['F', 'H']
        graph['D'] = ['F', 'A']
        graph['E'] = ['B', 'G']
        graph['F'] = ['B', 'D', 'C']
        graph['G'] = ['A', 'E']
        graph['H'] = ['C']
        result = bfs(graph, 'A')
        print(result.keys())
        # dict_keys(['A', 'B', 'G', 'D', 'F', 'E', 'C', 'H'])
        #           ['A', 'B', 'D', 'G', 'E', 'F', 'C', 'H']
