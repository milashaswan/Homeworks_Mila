from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Inpute time work: "))
    rate = int(input("Inpute ratet: "))
    prize = int(input("Inpute prize: "))
    print((time_work * rate) + prize)