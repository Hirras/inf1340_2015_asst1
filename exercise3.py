#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Hirra and Tyler'


def diagnose_car():

    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: answer

    Expected Outputs: diagnostic

    Errors:

    """
    answer = raw_input("Is the car silent when you turn the key? ")
    if answer == "y":
        answer = raw_input("Are the battery terminals corroded? ")
        if answer == "y":
            print ("Clean terminals and try starting again")
        elif answer == "n":
            print("The battery cables may be damaged. Replace cables and try again.")
    elif answer == "n":
        answer = raw_input("Does the car make a clicking noise? ")
        if answer == "y":
            print ("Replace the battery.")
        elif answer == "n":
            answer = raw_input("Does the car crank up but fail to start? ")
            if answer == "y":
                print ("Check spark plug connections.")
            elif answer == "n":
                answer = raw_input("Does the engine start and then die? ")
                if answer == "y":
                    answer = raw_input("Does the car have fuel injection? ")
                    if answer == "y":
                        print ("Get it in for service.")
                    elif answer == "n":
                        print ("Check to ensure the choke is opening and closing.")
                elif answer == "n":
                    print ("Your car is functioning.")
                else:
                    print("Invalid input. Please enter \"y\" or \"n\".")
            else:
                print("Invalid input. Please enter \"y\" or \"n\".")
        else:
            print("Invalid input. Please enter \"y\" or \"n\".")
    else:
        print("Invalid input. Please enter \"y\" or \"n\".")

diagnose_car()
