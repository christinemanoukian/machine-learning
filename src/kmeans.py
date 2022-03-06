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
        print(self.centers)

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
        print(self.clusters)

    def run(self):
        prev_clusters = {}
        while prev_clusters != self.clusters:
            prev_clusters = self.clusters.copy()
            self.find_centers()
            self.update_clusters()






data = [[-1,2], [1,0], [2,4]]

initial_clusters = {
    1: [0,2],
    2: [1],
    }

kmeans = KMeans(initial_clusters, data)
kmeans.run()
print(kmeans.clusters)