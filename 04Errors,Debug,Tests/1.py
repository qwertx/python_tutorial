def fact(n):
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)