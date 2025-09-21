#!/usr/bin/env python3
"""Maximize battery profit."""
from heapq import nlargest, heapify

def parse_input(filename):
    """Read input file"""
    with open(filename, "r") as f:
        return [int(price) for price in f.readlines()]

def optimize_array(prices)-> tuple|None:
    """
    If we can do two charges a day:
    """
    _max=max(prices)
    _max_idx=prices.index(_max)
    if _max_idx==0:
        return None
    _min=min(prices[:_max_idx])
    _min_idx=prices.index(_min)
    if _max_idx>_min_idx:
        return _max-_min, _min_idx, _max_idx

def optimize2(prices)->int|None:
    """
    If we can only do two charges a day: 
    """
    results=0
    results1=optimize_array(prices)
    if results1:
        profit1, min1, max1=results1
        results2=optimize_array(prices[:min1])
        results3=optimize_array(prices[max1+1:])

        if results2:
            profit2, _, _=results2
            results=max(results, profit1+profit2)
        if results3:
            profit3, _, _=results3
            results=max(results, profit1+profit3)
        return results

def optimize(prices)->int:
    """
    If we can only do two charges a day 
    """
    profits=[prices[i+1]- prices[i] for i in range(len(prices)-1) if prices[i] < prices[i+1]]
    heapify(profits)
    return sum(nlargest(2, profits))


if __name__ == "__main__":
    prices = parse_input("input.txt")
    profit1 = optimize(prices)
    profit2 = optimize2(prices) or 0
    print(profit1, profit2)
    profit = max(profit1, profit2)
    print(profit)
