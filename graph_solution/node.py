class Node:
    def __init__(self, name):
        self._name = name
        self._is_visited = False

    @property
    def name(self):
        return self._name

    @property
    def is_visited(self):
        return self._is_visited

    @is_visited.setter
    def is_visited(self, visit: bool):
        self._is_visited = visit

    def __eq__(self, other):
        if not (isinstance(other, Node)): return False
        return other.name == self.name

    def __str__(self):
        return self._name

    def __hash__(self):
        return hash(self._name)
