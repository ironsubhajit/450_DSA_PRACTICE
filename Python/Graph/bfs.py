from collections import defaultdict


class Graph:

    # Constructor
    def __int__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)