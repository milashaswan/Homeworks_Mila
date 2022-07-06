time_sec = int(input("Введите время в секундах:"))
hours = time_sec // 3600
minutes = (time_sec - hours * 3600) // 60
sec = time_sec - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс  {hours} : {minutes} : {sec}")