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
    if answer == "Y":
        answer = raw_input("Are the battery terminals corroded? ")
        if answer == "Y":
            print ("Clean terminals and try starting again.")
        elif answer == "N":
            print("Replace cables and try again.")
    elif answer == "N":
        answer = raw_input("Does the car make a clicking noise? ")
        if answer == "Y":
            print ("Replace the battery.")
        elif answer == "N":
            answer = raw_input("Does the car crank up but fail to start? ")
            if answer == "Y":
                print ("Check spark plug connections.")
            elif answer == "N":
                answer = raw_input("Does the engine start and then die? ")
                if answer == "Y":
                    answer = raw_input("Does the car have fuel injection? ")
                    if answer == "Y":
                        print ("Get it in for service.")
                    elif answer == "N":
                        print ("Check to ensure the choke is opening and closing.")
                elif answer == "N":
                    print ("Engine is not getting enough fuel. Clean fuel pump.")
                else:
                    print("Invalid input. Please enter \"y\" or \"n\".")
            else:
                print("Invalid input. Please enter \"y\" or \"n\".")
        else:
            print("Invalid input. Please enter \"y\" or \"n\".")
    else:
        print("Invalid input. Please enter \"y\" or \"n\".")

# diagnose_car()

""" Test Cases

Test Case 1
Is the car silent when you turn the key? y
Are the battery terminals corroded? y
Clean terminals and try starting again

Test Case 2
Is the car silent when you turn the key? y
Are the battery terminals corroded? n
The battery cables may be damaged. Replace cables and try again.

Test Case 3
Is the car silent when you turn the key? n
Does the car make a clicking noise? y
Replace the battery.

Test Case 4
Is the car silent when you turn the key? n
Does the car make a clicking noise? n
Does the car crank up but fail to start? y
Check spark plug connections.

Test Case 5
Is the car silent when you turn the key? n
Does the car make a clicking noise? n
Does the car crank up but fail to start? n
Does the engine start and then die? n
Engine is not getting enough fuel. Clean fuel pump.

Test Case 6
Is the car silent when you turn the key? n
Does the car make a clicking noise? n
Does the car crank up but fail to start? n
Does the engine start and then die? y
Does the car have fuel injection? y
Get it in for service.

Test Case 7
Is the car silent when you turn the key? n
Does the car make a clicking noise? n
Does the car crank up but fail to start? n
Does the engine start and then die? y
Does the car have fuel injection? n
Check to ensure the choke is opening and closing.

Test Case 8
Is the car silent when you turn the key? g
Invalid input. Please enter "Y" or "N".

"""
