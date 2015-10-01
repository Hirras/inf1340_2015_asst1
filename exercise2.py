#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: sides

    Expected Outputs: shape

    Errors: error


    """
    sides = raw_input("Insert the number of sides: ")
    if sides == "3":
        print ("triangle")
    elif sides == "4":
        print ("square")
    elif sides == "5":
        print ("pentagon")
    elif sides == "6":
        print ("hexagon")
    elif sides == "7":
        print ("heptagon")
    elif sides == "8":
        print ("octagon")
    elif sides == "9":
        print ("nonagon")
    elif sides == "10":
        print ("decagon")
    else:
        print("Error")


name_that_shape()
