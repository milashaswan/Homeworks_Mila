def my_func(x, y, z):
    sal = [x, y, z]
    total = []
    max_1 = max(sal)
    total.append(max_1)
    sal.remove(max_1)
    max_2 = max(sal)
    total.append(max_2)
    print(sum(total))
my_func(88, 8, 72)