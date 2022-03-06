from math import sqrt
from statistics import mode

class KNearestNeigborsClassifier:
    def __init__(self, k):
        self.k = k
        self.dict = {}
        self.distances = []
        self.classification = None

    def fit(self, portions, types, classification_index):
        types_dict = {}
        new_dict = {}
        for element in types:
            types_dict[element] = types.count(element)
            new_dict[element] = []
        for key in new_dict:
            index = types_dict.get(key)
            new_dict[key] = portions[:index]
            del portions[:index]
        for key in new_dict:
            for values in new_dict.get(key):
                for value in values:
                    value = float(value)
        self.dict = new_dict

    def compute_distances(self, point):
        other_points_lst = []
        other_points = []
        for key in self.dict:
            other_points_lst.append(self.dict.get(key))
        for lst in other_points_lst:
            for smaller_lst in lst:
                other_points.append(smaller_lst)
        distances = []
        for lst in other_points:
            distance = 0
            for i in range(len(point)):
                distance += (point[i] - lst[i]) ** 2
            distance = sqrt(distance)
            distances.append(distance)
        distances = [round(num, 3) for num in distances]
        self.distances = distances
        all_values = []
        for key in self.dict:
            for values in self.dict.get(key):
                all_values.append(values)
        for i in range(len(all_values)):
            all_values[i].insert(0, distances[i])
        for key in self.dict:
            index = len(self.dict.get(key))
            self.dict[key] = all_values[:index]
            del all_values[:index]
        return distances
    
    def classify(self, point):
        distances = self.distances
        neighbors = []
        types = []
        count = 1
        while count <= self.k:
            neighbors.append(min(distances))
            distances.remove(min(distances))
            count += 1
        for key in self.dict:
            values = self.dict.get(key)
            for i in range(len(values)):
                if values[i][0] in neighbors:
                    types.append(key)
        nearest_neighbor = ''
        nearest_neighbor = mode(types)
        self.classification = nearest_neighbor
