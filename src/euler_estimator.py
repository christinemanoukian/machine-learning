class EulerEstimator:
    def __init__(self, derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self, point):
        return self.derivative(point[0])

    def calc_estimated_points(self, point, step_size, num_steps):
        answer = [point]
        while num_steps > 0:
            point = list(point)
            point[1] += step_size * derivative(point[0])
            point[0] += step_size
            point = tuple(point)
            answer.append(point)
            num_steps -= 1
        return answer


def derivative(t):
    return t+1

euler = EulerEstimator(derivative)
print(euler.calc_derivative_at_point((1,4)))
print(euler.calc_estimated_points((1,4), .5, 4))