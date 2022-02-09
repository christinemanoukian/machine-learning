from math import sqrt

class KMeans:
    def __init__(self, initial_clusters, data):
        self.clusters = initial_clusters
        self.data = data
        self.centers = None

    def find_centers(self):
        length = len(self.data[0])
        centers = {k:[0 for i in range(length)] for k in self.clusters}
        for key, cluster in self.clusters.items():
            for index in cluster:
                for i in range(length):
                    centers[key][i] += self.data[index][i] / len(cluster)
        self.centers = centers

    def calc_dist(self, point1, point2):
        distance = 0
        for i in range(len(point1)):
            distance += (point2[i] - point1[i])**2
        distance = sqrt(distance)
        return distance

    def update_clusters(self):
        new_clusters = {k:[] for k in self.clusters}
        total_points = len(self.data)
        for index in range(total_points):
            distances = {k:self.calc_dist(self.data[index], self.centers[k]) for k in self.clusters}
            new_cluster = min(distances, key=lambda k: distances[k]) 
            new_clusters[new_cluster].append(index)
        self.clusters = new_clusters

    def run(self):
        prev_clusters = {}
        while prev_clusters != self.clusters:
            prev_clusters = self.clusters.copy()
            self.find_centers()
            self.update_clusters()






data = [[0.14, 0.14, 0.28, 0.44], 
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
         [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

initial_clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
    }

#kmeans = KMeans(initial_clusters, data)
#kmeans.run()
#print(kmeans.clusters)