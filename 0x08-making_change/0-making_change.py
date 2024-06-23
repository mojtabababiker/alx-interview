#!/usr/bin/python3
"""
Solving the classic coin change problem
"""


def makeChange(coins, total):
    """
    Determine the minimum number of cions needed to meet the
    total
    Parameters:
    -----------
    coins: a list of coins(change) that we have
    total: the total amount we gonna change it

    Returns:
    -----------
    int: the minimum number of coins to meet total
         0 if total is <= 0
         -1 if coins can't meet total
    """
    cached_mins = {
        0: 0
    }

    if total <= 0:
        return 0

    for sub_total in range(1, total + 1):
        for coin in coins:
            min_ = sub_total - coin
            if min_ >= 0:
                cached_min = cached_mins.get(sub_total, total + 1)
                last_min = cached_mins.get(min_, total + 1)
                cached_mins[sub_total] = min(last_min + 1, cached_min)

    if cached_mins.get(total, total + 1) == total + 1:
        return -1
    return cached_mins.get(total)


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))

    print(makeChange([1], 11))

    print(makeChange([1, 2, 5, 10, 20, 50, 100, 500, 1000], 70))

    print(makeChange([1, 2, 5, 10, 20, 50, 100, 500, 1000], 121))
