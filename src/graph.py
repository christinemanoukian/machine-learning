class Graph:
    def __init__(self, edges):
        self.edges = edges

    def get_children(self, node):
        result = []
        for edge in self.edges:
            if edge[0] == node:
                result.append(edge[1])
        return result

    def get_parents(self, node):
        result = []
        for edge in self.edges:
            if edge[1] == node:
                result.append(edge[0])
        return result
