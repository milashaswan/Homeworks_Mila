def my_f():
    try:
        with open('file_5.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
my_f()y_f()