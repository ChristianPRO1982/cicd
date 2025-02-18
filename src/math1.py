# addition
def add(x, y):
    return x + y

# soustraction
def sub(x, y):
    return x - y

# multiplications
def mul(x, y):
    return x * y

# division
def div(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y