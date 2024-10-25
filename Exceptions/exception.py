# SyntaxError -  error you typed

# How to escape value error and name error, if wrong data entered
try:
    x = int(input("What's x?: "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
