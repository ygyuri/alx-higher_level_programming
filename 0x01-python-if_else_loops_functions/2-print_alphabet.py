#!/usr/bin/python3
# 2-print_alphabet.py

"""Print alphabets in lowercase, a new line  should not follow."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
