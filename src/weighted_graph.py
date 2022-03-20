import sys
sys.path.append('src')
from graph import *

class WeightedGraph:
    def __init__(self, weights):
        self.weights = weights
        self.nodes = {}
        self.edges = [edge for edge in weights]
        for edge in self.edges:
            if edge[0] not in self.nodes:
                self.nodes[edge[0]] = Node(edge[0])
            if edge[1] not in self.nodes:
                self.nodes[edge[1]] = Node(edge[1])

    def get_children(self, node):
        return [self.nodes[edge[1]] for edge in self.edges if edge[0] == node.index]

    def calc_distance(self, starting_node_index, ending_node_index):
        current_node = self.nodes[starting_node_index]
        for node in self.nodes:
            self.nodes[node].distance = 9999999999
        current_node.distance = 0
        visited = []
        # print(self.get_children(current_node.index)) #When I print this here it prints the correct thing which is [4,0]
        while current_node.index != ending_node_index:
            # print(self.get_children(current_node.index)) #if i print it inside the while loop it prints [8,3] an infinite amount of times
            for child in self.get_children(current_node):
                # print(child) #Here it's printing 8 and 3 and infinite amount of times and idk why
                if child not in visited:
                    child.distance = min(child.distance, current_node.distance + self.weights[(current_node.index, child.index)])
                    visited.append(child)
            #print(visited)
            closest_node = None
            for node in visited:
                if closest_node is None:
                    closest_node = node
                if node in visited:
                    if node.distance < closest_node.distance:
                        closest_node = node
            current_node = closest_node
        return current_node.distance


#    def calc_shortest_path(self, starting_node_index, ending_node_index):


weights = {
    (0,1): 3, (1,0): 3,
    (1,7): 4, (7,1): 4,
    (7,2): 2, (2,7): 2,
    (2,5): 1, (5,2): 1,
    (5,6): 8, (6,5): 8,
    (0,3): 2, (3,0): 2,
    (3,2): 6, (2,3): 6,
    (3,4): 1, (4,3): 1,
    (4,8): 8, (8,4): 8,
    (8,0): 4, (0,8): 4
}
weighted_graph = WeightedGraph(weights)
print(weighted_graph.calc_distance(8,7))