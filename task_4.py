my_str = input("введите строку из нескольких слов, разделенных пробелами ")
my_text = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_text = my_str.split()
    if len(str(my_text)) <= 10:
        print(f" {num} {my_text [el]}")
        num += 1
    else:
        print(f" {num} {my_text [el] [0:10]}")
        num += 1