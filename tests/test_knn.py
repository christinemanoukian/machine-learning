import sys
sys.path.append('src')
from k_nearest_neighbors import KNearestNeigborsClassifier

knn = KNearestNeigborsClassifier(k=5)
X = [[.14, .14, .28, .44], [.10, .18, .28, .44], [.12, .10, .33, .45], [.10, .25, .25, .40], [.00, .10, .40, .50], [.00, .20, .40, .40], [.10, .08, .35, .47], [.00, .05, .30, .65], [.20, .00, .40, .40], [.25, .10, .30, .35], [.22, .15, .50, .13], [.15, .20, .35, .30], [.22, .00, .40, .38]]
y = ['Shortbread', 'Shortbread', 'Shortbread', 'Shortbread', 'Sugar', 'Sugar', 'Sugar', 'Sugar', 'Fortune', 'Fortune', 'Fortune', 'Fortune', 'Fortune']
knn.fit(X, y, classification_index = 0)
observation1 = [.10, .15, .30, .45]
knn.compute_distances(observation1)
if knn.classify(observation1) != 'Shortbread':
    print('classify failed on input observation1')
observation2 = [.14, .18, .12, .25]
knn.compute_distances(observation2)
if knn.classify(observation2) != 'Shortbread':
    print('classify failed on input obvservation2')
observation3 = [.44, .28, .33, .40]
if knn.classify(observation3) != 'Shortbread':
    print('classify failed on input observation3')