class EulerEstimator:
    def __init__(self, derivatives):
        self.derivatives = derivatives

    def calc_derivative_at_point(self, point):
        answer = point[1]
        old_states = {}
        for key in answer:
            old_states[key] = answer[key]
        for key in answer:
            answer[key] = derivatives[key](point[0], old_states)
        return answer

    def calc_estimated_points(self, point, step_size, num_steps):
        answer = [point]
        while num_steps > 0:
            new_point = list(answer[-1])
            new_point[1] = dict(new_point[-1])
            old_states = {}
            for key in new_point[1]:
                old_states[key] = new_point[1][key]
            for key in new_point[1]:
                new_point[1][key] += step_size * derivatives[key](new_point[0], old_states)
            new_point[0] += step_size
            new_point = tuple(new_point)
            answer.append(new_point)
            num_steps -= 1
        t = []
        a = []
        b = []
        c = []
        for point in answer:
            t.append(point[0])
            a.append(point[1]['a'])
            b.append(point[1]['b'])
            c.append(point[1]['c'])
        print(t)
        print(a)
        print(b)
        print(c)
        return answer


initial_state = {'a': -.45, 'b': -.05, 'c': 0}
initial_point = (-.4, initial_state)

def da_dt(t, state):
    return state['a'] + 1

def db_dt(t, state):
    return state['a'] + state['b']

def dc_dt(t, state):
    return 2 * state['b'] + 3*t

derivatives = {
    'a': da_dt,
    'b': db_dt,
    'c': dc_dt
}

euler = EulerEstimator(derivatives)
#print(euler.calc_derivative_at_point(initial_point))
print(euler.calc_estimated_points(initial_point, .01, 100))
