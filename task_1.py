my_list = [77, -77, 'True', True, 9.5,  None, 'list']
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)