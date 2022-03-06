class Node:
    def __init__(self, index):
        self.index = index
        self.distance = 0
        self.previous = None

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

    def set_distance_and_previous(self, start_index):
        queue = [start_index]
        visited = {}
        order = []
        while queue != []:
            node = queue[0]
            order.append(node)
            visited[node] = True
            current_node = Node(node)
            for child in self.get_children(node):
                if child not in visited and child not in queue:
                    queue.append(child)
                    self.previous = current_node
                    self.distance = current_node.distance + 1
            queue.remove(queue[0])
        return order


    def calc_distance(self, starting_node_index, ending_node_index):
        self.set_distance_and_previous(starting_node_index)
        ending_node = Node(ending_node_index)
        if ending_node_index not in self.set_distance_and_previous(starting_node_index):
            return False
        else:
            return ending_node.distance



graph = Graph([(0,1), (1,2), (1,4), (4,5), (4,3), (3,1), (3,6)])
print(graph.calc_distance(0, 3))