#!/usr/bin/python3
"""
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
