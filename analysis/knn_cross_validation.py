import sys
sys.path.append('src')
from k_nearest_neighbors import KNearestNeigborsClassifier
KNN = KNearestNeigborsClassifier
import matplotlib.pyplot as plt
import numpy as np


def knn(data):
    k_dict = {}
    for k in range(1, len(data)):
        KNN = KNearestNeigborsClassifier(k)
        count = 0
        ind = 0
        while ind < len(data):
            current_point = data[ind]
            current_point_values = data[ind][1:]
            classification = current_point[0]
            data.remove(current_point)
            types = []
            portions = []
            for point in data:
                types.append(point[0])
                portions.append(point[1:])
            KNN.fit(portions, types, classification_index=0)
            KNN.compute_distances(current_point_values)
            KNN.classify(current_point_values)
            if KNN.classification == classification:
                count += 1
            data.insert(0, current_point)
            ind += 1
        k_dict[k] = count
    return k_dict


data = [
['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]]


print(knn(data))

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
y = [8,14,8,11,10,6,8,7,9,6,10,7,10,7,6,7,8,8]
plt.plot(x, y)
plt.xticks(np.arange(0, 19, 1.0))
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.savefig('knn_graph.png')