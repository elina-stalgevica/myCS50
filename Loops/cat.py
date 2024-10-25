# How many times need to print mweow
# 2 options - for i in [0, 1, 2, 3] or for i in range (3)
for i in range (3):
    print("Meow")

#Or use multiplication operator in print function
# Add end="" so you dont have extra blank line at the end
print("Meow\n" * 3, end="")

# If user gives input on how many times
while True:
    n = int(input("What's n: "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")

