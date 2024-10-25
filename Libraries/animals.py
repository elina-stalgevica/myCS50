# Cowsay -  a program that can be installed. Use: pip install cowsay
# SYS - default exists for you
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

# Cowsay also come with other function - cowsay.trex (Yes, a trex)
