#!/usr/bin/python3
""" writting a function that prints a square with the character #.

def print_square(size):
"""A function to print square
size(int): th height/width of the square
Raises:
    TypeError: if size is not an interger 
    ValueError: if size less than 0 or < 0.
    """
    if not((isinstance(size, int))):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")



