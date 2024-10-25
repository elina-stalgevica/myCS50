# sys - short for  System-specific parameters and functions

# sys.argv - Argument vector - the list of the words that the human typed in their prompt before they hit enter.

import sys

# Check for error
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# We wnter [1] not [0], because in sys.argv [0] is "name.py", but [1] "Elina"
# Sys.exit - print out and exit without index error/name error

