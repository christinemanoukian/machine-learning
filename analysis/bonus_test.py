def partial_a(a, b, c):
    return 2*(a+b+c)+8*(4*a+2*b+c-1)+18*(9*a+3*b+c-1)

def partial_b(a, b, c):
    return 2*(a+b+c)+4*(4*a+2*b+c-1)+6*(9*a+3*b+c-1)

def partial_c(a, b, c):
    return 2*(c-2)+2*(a+b+c)+2*(4*a+2*b+c-1)+2*(9*a+3*b+c-1)

def reduce_rss(a, b, c, alpha, num_iterations):
    a_old = a
    b_old = b
    c_old = c
    while num_iterations > 0:
        a_new = a_old - alpha * partial_a(a_old, b_old, c_old)
        b_new = b_old - alpha * partial_b(a_old, b_old, c_old)
        c_new = c_old - alpha * partial_c(a_old, b_old, c_old)
        a_old = a_new
        b_old = b_new
        c_old = c_new
        num_iterations -= 1
    rss = (c_old-2)**2 + (a_old+b_old+c_old)**2 + (4*a_old+2*b_old+c_old-1)**2 + (9*a_old+3*b_old+c_old-1)**2
    return rss

print(reduce_rss(1, 0, 0, .008, 500))