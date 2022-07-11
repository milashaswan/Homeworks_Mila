my_list = [7, 5, 3, 3, 2]
n = int(input("Введите число: "))
a = my_list.count(n)
for i in my_list:
    if a > 0:
        i = my_list.index(n)
        my_list.insert(i+a, n)
        break
    elif n > i:
            i = my_list.index(i)
            my_list.insert(i, n)
            break
    elif n < my_list[len(my_list) - 1]:
            my_list.append(n)
print(my_list)