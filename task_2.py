list_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [j for i, j in zip(list_number, list_number[1:]) if j > i]
print("Start List: " + str(list_number))
print("New List: " + str(new_list))