class Node:
    def __init__(self, index):
        self.index = index
        self.distance = 0
        self.previous = None

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = {}
        for edge in edges:
            if edge[0] not in self.nodes:
                self.nodes[edge[0]] = Node(edge[0])
            if edge[1] not in self.nodes:
                self.nodes[edge[1]] = Node(edge[1])

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
        visited = {start_index: True}
        order = [start_index]
        while queue != []:
            node = queue[0]
            current_node = self.nodes[node]
            for child in self.get_children(node):
                if child not in visited and child not in queue:
                    queue.append(child)
                    self.nodes[child].previous = current_node
                    self.nodes[child].distance = current_node.distance + 1
                    order.append(child)
                    visited[child] = True
            queue.remove(queue[0])
        return order

    def calc_distance(self, starting_node_index, ending_node_index):
        self.set_distance_and_previous(starting_node_index)
        ending_node = self.nodes[ending_node_index]
        if ending_node_index not in self.set_distance_and_previous(starting_node_index):
            return False
        else:
            return ending_node.distance

    def calc_shortest_path(self, starting_node_index, ending_node_index):
        self.set_distance_and_previous(starting_node_index)
        if self.calc_distance(starting_node_index, ending_node_index) == False:
            return False
        else:
            path = [ending_node_index]
            current_node = self.node[ending_node_index]
            ending_node = self.nodes[starting_node_index]
            while current_node != ending_node:
                current_node = current_node.previous
                path.append(current_node.id)
            return path[::-1]