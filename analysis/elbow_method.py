import sys
sys.path.append('src')
from kmeans import KMeans
import matplotlib.pyplot as plt

def sum_of_errors(point1, point2):
    answer = 0
    for i in range(len(point1)):
        answer+= (point2[i]-point1[i])**2
    return answer

def calc_error(k_value, data):
    initial_clusters = {k+1:[i for i in range(k, len(data), k_value)] for k in range(k_value)}
    kmeans = KMeans(initial_clusters, data)
    kmeans.run()
    total_squared_error = 0
    for center in kmeans.centers:
        squared_error = 0
        for row in kmeans.clusters[center]:
            squared_error += sum_of_errors(kmeans.centers[center], data[row])
        total_squared_error += squared_error
    return total_squared_error


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

k_values = [k for k in range(1,5)]
error = [calc_error(k, data) for k in k_values]


plt.plot(k_values, error)
plt.xlabel('k')
plt.ylabel('error')
plt.savefig('elbow_method.png')