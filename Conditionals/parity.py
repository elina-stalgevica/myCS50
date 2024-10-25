# Remainder (%) operator helps to understand if number is even.
# Even numbers - Can be divided by 2 (Divided by remainder and left with no leftover)

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # Example how to put 4 lines in 1 without IF/ELSE
    return n % 2 == 0

main()

