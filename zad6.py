def newton(x, estimate):
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference > TOLERANCE:
        estimate = newton(x, estimate)
    return estimate