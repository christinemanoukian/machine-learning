def minimize(gradient, initial_point, alpha, num_iterations):
    while num_iterations > 0:
        count = 0
        while count < len(initial_point):
            initial_point[count] = initial_point[count] - alpha * gradient(initial_point)[count]
            count += 1
        num_iterations -= 1
    return initial_point

def gradient(x):
    x[0] = 2*x[0] + 2
    x[1] = 2*x[1] + 2
    return x


print(minimize(gradient, [1,0], .01, 100))
