def my_func(a):
    separate = a.split(' ')
    total = []
    for i in separate:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func(input("Enter smth")))