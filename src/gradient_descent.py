def minimize(gradient, initial_point, alpha, num_iterations):
    for point in initial_point:
        point = point
    while num_iterations > 0:
        for point in initial_point:
            point[0] = point[0] - alpha * gradient(point[0])
        num_iterations -= 1
    return initial_point

def gradient(x):
    return 2*x + 2
