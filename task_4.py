en = ['One', 'Two', 'Three', 'Four']
ru = ['Один', 'Два', 'Три', 'Четыре']
with open('text_4.txt') as file:
    data = file.read()
for i, word in enumerate(en):
    if word in data:
        data = data.replace(word, ru[i])
with open('textRU.txt', 'w') as file:
    file.write(data)
if __name__ == '__main__':
    print(data)