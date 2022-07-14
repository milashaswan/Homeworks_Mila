def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    except ValueError:
        return "Enter only number"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))