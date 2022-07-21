def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res
a = fact(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))