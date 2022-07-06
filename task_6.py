a = int(input("Результат в первый день в км "))
b = int(input("Желаемый результат "))
day = 1
km = a
while km < b:
    a = a + a * 0.1
    day += 1
    km = a
print(f"В день {day} вы достигните  желаемого результата")