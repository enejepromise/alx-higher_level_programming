#!/usr/bin/python3
""" Definition of a function that adds 2 integers."""


def add_integers(a, b=98):
    return addition of a and b
""" a and b must be first casted to integers if they are float"""
raise:
    TypeError: if either of a and b is non-integers and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise: TypeError ("a must be an integer")
    if ((not isintance(b, int) and not isinstance(b, float))):
        raise: TypeError ("b must an integer")
    return (int(a) +  int(b))
