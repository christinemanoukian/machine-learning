def partial_a(a, b):
    return 34*a+10*b-46

def partial_b(a, b):
    return 10*a+4*b-16

def reduce_rss(a, b, alpha, num_iterations):
    a_old = a
    b_old = b
    while num_iterations > 0:
        a_new = a_old - alpha * partial_a(a_old, b_old)
        b_new = b_old - alpha * partial_b(a_old, b_old)
        a_old = a_new
        b_old = b_new
        num_iterations -= 1
    print(a_old)
    print(b_old)


print(reduce_rss(1, 0, .01, 2))