def my_func(x,y):
    v1 = x ** y
    v2 = 1
    i = 1
    while i <= abs(y):
        v2 *= x
        i += 1

    return v1, 1 / v2

print(
    my_func(
        int(input(" Введите действительное число v1: ")),
        int(input(" Введите отрицательное число v2: "))
    )
)