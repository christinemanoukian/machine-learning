import sys
sys.path.append('src')
from k_nearest_neighbors import KNearestNeigborsClassifier
KNN = KNearestNeigborsClassifier
import matplotlib.pyplot as plt
import numpy as np
from statistics import *

def no_normalization(data):
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

def simple_scale(data):
    for lst in data:
        lst[1] = lst[1] / 496.0
        lst[2] = lst[2] / 9904.0
        lst[3] = lst[3] / 39.5
        lst[4] = lst[4] / 8.0
    return no_normalization(data)

def min_max(data):
    for lst in data:
        lst[1] = (lst[1]-50.0) / (496.0-50.0)
        lst[2] = (lst[2]-1087.0) / (9904.0-1087.0)
        lst[3] = (lst[3]-5.0) / (39.5-5.0)
        lst[4] = (lst[4]-3.0) / (8.0-3.0)
    return no_normalization(data)

def z_score(data):
    for lst in data:
        lst[1] = (lst[1]-261.42) / 117.4145018833928
        lst[2] = (lst[2]-4912.94) / 2403.5401450125332
        lst[3] = (lst[3]-18.185) / 9.861314836421679
        lst[4] = (lst[4]-5.095) / 1.3605090402069544
    return no_normalization(data)


data = [
["children's book", 346.0, 6306.0, 9.2, 3.5],
["children's book", 229.0, 3835.0, 12.8, 3.6],
["children's book", 217.0, 5084.0, 14.1, 4.0],
["children's book", 149.0, 6291.0, 11.2, 3.5],
["children's book", 368.0, 7879.0, 13.1, 4.8],
["children's book", 159.0, 6109.0, 14.0, 4.4],
["children's book", 215.0, 1705.0, 9.3, 4.2],
["children's book", 370.0, 7766.0, 9.8, 4.7],
["children's book", 141.0, 6635.0, 10.5, 3.0],
["children's book", 302.0, 3792.0, 13.2, 4.3],
["children's book", 50.0, 4455.0, 13.7, 3.5],
["children's book", 164.0, 7093.0, 6.9, 4.1],
["children's book", 134.0, 7773.0, 13.0, 3.9],
["children's book", 78.0, 3240.0, 10.1, 4.9],
["children's book", 88.0, 4859.0, 12.1, 4.1],
["children's book", 335.0, 4782.0, 14.6, 4.2],
["children's book", 256.0, 4115.0, 11.0, 3.8],
["children's book", 251.0, 3032.0, 6.9, 3.4],
["children's book", 264.0, 5597.0, 9.8, 3.2],
["children's book", 315.0, 7137.0, 14.2, 4.7],
["children's book", 364.0, 7462.0, 10.4, 3.8],
["children's book", 297.0, 2929.0, 13.1, 4.7],
["children's book", 363.0, 5129.0, 14.5, 4.2],
["children's book", 208.0, 5622.0, 15.0, 4.8],
["children's book", 328.0, 1577.0, 11.1, 4.0],
["children's book", 271.0, 6916.0, 7.4, 4.5],
["children's book", 91.0, 2543.0, 12.9, 3.7],
["children's book", 336.0, 1704.0, 6.5, 4.4],
["children's book", 66.0, 5017.0, 14.1, 4.1],
["children's book", 288.0, 1187.0, 11.3, 4.2],
["children's book", 252.0, 3738.0, 8.7, 5.0],
["children's book", 63.0, 1151.0, 14.6, 3.4],
["children's book", 93.0, 2474.0, 13.0, 4.9],
["children's book", 58.0, 3979.0, 6.0, 3.5],
["children's book", 127.0, 5528.0, 8.5, 3.4],
["children's book", 226.0, 1276.0, 6.0, 5.0],
["children's book", 120.0, 3510.0, 12.3, 4.7],
["children's book", 371.0, 2186.0, 11.7, 4.9],
["children's book", 70.0, 5733.0, 13.5, 3.7],
["children's book", 138.0, 5178.0, 9.4, 3.3],
["children's book", 215.0, 3869.0, 10.7, 4.0],
["children's book", 159.0, 3500.0, 13.4, 3.5],
["children's book", 246.0, 1087.0, 12.4, 3.7],
["children's book", 66.0, 2966.0, 7.4, 4.9],
["children's book", 173.0, 3015.0, 8.6, 4.9],
["children's book", 272.0, 5348.0, 12.2, 3.8],
["children's book", 195.0, 5556.0, 5.0, 3.4],
["children's book", 167.0, 2676.0, 11.4, 3.8],
["children's book", 356.0, 4977.0, 9.1, 3.8],
["children's book", 296.0, 3928.0, 11.6, 3.1],
['adult book', 278.0, 3703.0, 14.7, 6.1],
['adult book', 295.0, 6272.0, 32.7, 7.5],
['adult book', 298.0, 4152.0, 24.0, 7.2],
['adult book', 450.0, 8406.0, 15.6, 8.0],
['adult book', 353.0, 2209.0, 31.8, 7.9],
['adult book', 261.0, 7267.0, 19.5, 4.9],
['adult book', 387.0, 1520.0, 34.7, 6.1],
['adult book', 139.0, 2511.0, 29.5, 7.5],
['adult book', 212.0, 9817.0, 13.0, 7.4],
['adult book', 259.0, 2191.0, 18.2, 5.8],
['adult book', 417.0, 8822.0, 14.0, 6.1],
['adult book', 360.0, 4450.0, 36.2, 5.1],
['adult book', 107.0, 1846.0, 30.4, 6.2],
['adult book', 479.0, 9477.0, 37.3, 4.2],
['adult book', 400.0, 7461.0, 29.7, 6.8],
['adult book', 461.0, 6941.0, 21.2, 6.2],
['adult book', 183.0, 6491.0, 10.3, 4.6],
['adult book', 233.0, 8212.0, 31.6, 5.4],
['adult book', 348.0, 1850.0, 14.9, 7.9],
['adult book', 216.0, 4856.0, 26.5, 5.2],
['adult book', 291.0, 3538.0, 11.4, 4.7],
['adult book', 309.0, 2102.0, 22.1, 5.3],
['adult book', 266.0, 2345.0, 37.3, 5.9],
['adult book', 436.0, 9798.0, 20.3, 5.9],
['adult book', 380.0, 5126.0, 19.1, 6.9],
['adult book', 458.0, 9317.0, 28.8, 5.5],
['adult book', 490.0, 6930.0, 12.0, 4.3],
['adult book', 400.0, 2020.0, 10.2, 5.6],
['adult book', 308.0, 5313.0, 24.7, 6.3],
['adult book', 372.0, 5096.0, 21.0, 8.0],
['adult book', 204.0, 8105.0, 22.9, 5.4],
['adult book', 126.0, 8840.0, 31.1, 7.6],
['adult book', 281.0, 7254.0, 13.6, 5.6],
['adult book', 183.0, 1858.0, 38.4, 4.9],
['adult book', 159.0, 3183.0, 21.3, 6.2],
['adult book', 161.0, 9904.0, 39.5, 4.6],
['adult book', 262.0, 7279.0, 36.3, 6.0],
['adult book', 467.0, 4241.0, 25.0, 6.0],
['adult book', 368.0, 3217.0, 28.3, 4.9],
['adult book', 236.0, 9682.0, 37.0, 7.3],
['adult book', 114.0, 2761.0, 17.7, 7.1],
['adult book', 437.0, 6455.0, 31.5, 7.2],
['adult book', 127.0, 2219.0, 36.1, 4.2],
['adult book', 190.0, 1845.0, 10.5, 7.4],
['adult book', 232.0, 2866.0, 14.5, 6.6],
['adult book', 487.0, 5792.0, 37.0, 6.0],
['adult book', 330.0, 7268.0, 34.2, 7.0],
['adult book', 496.0, 7849.0, 37.2, 4.8],
['adult book', 314.0, 6588.0, 34.8, 5.9],
['adult book', 416.0, 4803.0, 27.6, 7.4],]


x = [i for i in range(1,100)]
y = [value for value in list(no_normalization(data).values())]

y_ss = [value for value in list(simple_scale(data).values())]

y_mm = [value for value in list(min_max(data).values())]

y_zs = [value for value in list(z_score(data).values())]



plt.plot(x, y, "-r", label="no normalization")
plt.plot(x, y_ss, "-y", label="simple scale")
plt.plot(x, y_mm, "-g", label="min max")
plt.plot(x, y_zs, "-b", label="z-score")
plt.legend(['no normalization', 'simple scale', 'min max', 'z-score'])
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.title('K vs ACCURACY')
plt.savefig('normalization.png')