import re

data_file = open("text_6.txt", "r")

predmety = {}

for line in data_file.readlines():
    predmet = line.split()[0]
    zaniatija = 0

    for x in re.findall('\d+', line):
        zaniatija += int(x)
    predmety.update({predmet: zaniatija})

print(predmety)
data_file.close()

