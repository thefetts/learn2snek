import math


def at_least(k, n, p):
    sum = 0
    iterator = k
    while iterator <= n:
        sum += exact(iterator, n, p)
        iterator += 1
    return sum


def exact(k, n, p):
    q = 1 - p
    return bi_co(n, k) * (p ** k) * (q ** (n - k))


def bi_co(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n - k))
