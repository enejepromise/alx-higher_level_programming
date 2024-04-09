#!/usr/bin/python3
""" Determining a function that prints My name is <first name> <last name>

def say_my_name(first_name, last_name=""):
    """Defining a function that accept first name and last name
    fist_name(str): first name to print
    last_name(str): last name to print
    Raises:
        TypeError: if either first_name or last_name is not a string

    """
    if not(isinstance(first_name, str)
        raise TypeError("first_name must be a string")
    if not(isinstance(last_name, str)
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
