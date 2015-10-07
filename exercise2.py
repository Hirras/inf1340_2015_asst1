#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Hirra and Tyler'

def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: sides

    Expected Outputs: shape

    Errors: error


    """

    # get user input of number of sides
    sides = raw_input("Insert the number of sides: ")

    # print shape name based on number of sides
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

""" Test cases:
Test case 1:
    Input: 3
    Expected output: triangle
    Actual output: triangle

Test case 2:
    Input: 4
    Expected output: square
    Actual output: square

Test case 3:
    Input: 5
    Expected output: pentagon
    Actual output: pentagon

Test case 4:
    Input: 6
    Expected output: hexagon
    Actual output: hexagon

Test case 5:
    Input: 7
    Expected output: heptagon
    Actual output: heptagon

Test case 6:
    Input: 8
    Expected output: octagon
    Actual output: octagon

Test case 7:
    Input: 9
    Expected output: nonagon
    Actual output: nonagon

Test case 8:
    Input: 10
    Expected output: decagon
    Actual output: decagon

Test case 9: 
    Input: x
    Expected output: Error
    Actual output: Error

Passed all tests successfully
"""

