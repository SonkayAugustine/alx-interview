#!/usr/bin/python3
"""
0-module: making_change.py
"""


def makeChange(coins, total):
    """
    return fewest number of coins needed to meet total
    """

    if total <= 0:
        return 0

    newVal = total + 1
    coinJar = {0: 0}

    for i in range(1, total + 1):
        coinJar[i] = newVal

        for coin in coins:
            immediate = i - coin
            if immediate < 0:
                continue

            coinJar[i] = min(coinJar[immediate] + 1, coinJar[i])

    if coinJar[total] == total + 1:
        return -1

    return coinJar[total]
