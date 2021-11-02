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

    def breadth_first(self, node):
        queue = [node]
        visited = {node: True}
        order = [node]
        while queue != []:
            for n in self.get_children(queue[0]):
                if n not in visited and n not in queue:
                    queue.append(n)
                    order.append(n)
                    visited[n] = True
            queue.remove(queue[0])
        return order
    
    def depth_first(self, node):
        stack = [node]
        visited = {node: True}
        order = []
        while stack != []:
            current = stack[0]
            stack.remove(current)
            visited[current] = True
            order.append(current)
            for n in self.get_children(current):
                if n not in visited and n not in stack:
                    stack.insert(0, n)
        return order
