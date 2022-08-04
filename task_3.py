with open('text_3.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
