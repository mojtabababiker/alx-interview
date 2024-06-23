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
    """
    ============== USING DYNAMIC PROGRAMMING ================
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
    ==========================================================
    """

    """
    ========================= USING MATH =====================
    """
    coins_num = 0

    if total <= 0:
        return 0

    for coin in sorted(coins, key=lambda e: -e):
        while (total - coin) >= 0:
            total -= coin
            coins_num += 1

    if total == 0:
        return coins_num
    return -1
