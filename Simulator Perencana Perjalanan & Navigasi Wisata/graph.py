class TravelGraph:
    def __init__(self):
        self.adj = {}
    def add_edge(self, u, v):
        if u not in self.adj: self.adj[u] = []
        if v not in self.adj: self.adj[v] = []
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

