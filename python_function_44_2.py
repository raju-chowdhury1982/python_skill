def add_num(var1, var2):
    num1 = float(var1)
    num2 = float(var2)
    if (type(num1) == type(1.0) and type(num2) == type(1.0)):
        return num1 + num2
    else:
        return ("improper input given")


print(add_num(10, 20))

print(add_num("10", "20"))

print(add_num(10, "20"))

print(add_num("10", 20))

# add_num(10, "a")

# add_num("b", 20)


