def minimize(fprime, x0, alpha, num_iterations):
    answer = x0
    while num_iterations > 0:
        answer = answer - alpha * fprime(answer)
        num_iterations -= 1
    return round(answer, 2)
