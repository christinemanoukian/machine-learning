from math import exp as e


def partial_a(a, b):
    return 2*(1/(1+e(a+b))-.5) * (-e(a+b))/((1+e(a+b))**2) + 2*(1/(1+e(4*a+b))-1) * (-4*e(4*a+b))/((1+e(4*a+b))**2)

def partial_b(a, b):
    return 2*(1/(1+e(b))) * -(e(b))/((1+e(b))**2) + 2*(1/(1+e(a+b))-.5) * -(e(a+b))/((1+e(a+b))**2) + 2*(1/(1+e(4*a+b))-1) * -(e(4*a+b))/((1+e(4*a+b))**2)

def reduce_rss(a, b, alpha, num_iterations):
    a_old = a
    b_old = b
    while num_iterations > 0:
        a_new = a_old - alpha * (partial_a(a_old, b_old))
        b_new = b_old - alpha * (partial_b(a_old, b_old))
        a_old = a_new
        b_old = b_new
        num_iterations -= 1
    print(a_old)
    print(b_old)
