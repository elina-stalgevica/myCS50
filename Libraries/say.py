# We can import our own module with functions frrom sayings.py

import sys

from sayings import hello

if len(sys.argv) == 2:
  hello(sys.argv[1])
