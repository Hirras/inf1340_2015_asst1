#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2015. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Hirra and Tyler'

# function to calculate net gain/loss of purchase
def calc_pur_cost(pur_num_shares, pur_share_cost, pur_comm_pct):
    net_pur_cost = pur_num_shares * pur_share_cost
    pur_comm_cost = net_pur_cost * (pur_comm_pct / 100)  # divide input percentage by 100 to make an accurate calculation
    total_pur_cost = net_pur_cost + pur_comm_cost
    return total_pur_cost

# function to calculate net gain/loss of sale
def calc_sale_cost(sale_num_shares, sale_share_cost, sale_comm_pct):
    net_sale_cost = sale_num_shares * sale_share_cost
    sale_comm_cost = net_sale_cost * (sale_comm_pct / 100)  # divide input percentage by 100 to make an accurate calculation
    total_sale_cost = net_sale_cost - sale_comm_cost
    return total_sale_cost

# function to take inputs and calculate total gain/loss
def calc_total_cost():
    pur_num_shares = float(raw_input("Number of shares purchased: "))
    pur_share_cost = float(raw_input("Purchase price per share: "))
    pur_comm_pct = float(raw_input("Purchase commission percentage (e.g., for 3% enter '3'): "))

    sale_num_shares = float(raw_input("Number of shares sold: "))
    sale_share_cost = float(raw_input("Sale price per share: "))
    sale_comm_pct = float(raw_input("Sale commission percentage (e.g., for 3% enter '3'): "))

    pur_cost = calc_pur_cost(pur_num_shares, pur_share_cost, pur_comm_pct)
    sale_cost = calc_sale_cost(sale_num_shares, sale_share_cost, sale_comm_pct)

    total_cost = sale_cost - pur_cost

    return total_cost

profit = calc_total_cost()

# output result to user
print(profit)

""" Test cases
Inputs:
    Number of shares purchased: 2000
    Purchase price per share: 900
    Purchase commission percentage: 3
    Number of shares sold: 2000
    Sale price per share: 942.75
    Sale commission percentage: 3

Expected output:
    Profit/loss: -25065.0

Actual output:
    Profit/loss: -25065.0
"""
