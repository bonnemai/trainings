#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'efficientJanitor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY weight as parameter.
#
from itertools import combinations
def validate(combs): 
    # for comb in combs:
    _sum=sum(combs)
    if _sum>3:
        return False
    return True

def count(combs): 
    results=0
    for comb in combs:
        results+=1
    return results

def efficientJanitor(weight):
    # Write your code here
    if len(weight)<1: 
        return 0
    weight.sort()
    left=0
    right=len(weight)-1
    results=0
    while left<=right:
        if left==right:
            results+=1
            break
        if weight[left]+weight[right]<=3:
            left+=1
            right-=1
            results+=1
        else: 
            right-=1
            results+=1
    return results
    # results=sys.maxsize
    # for i in range( len(weight)-1, 0, -1): 
    #     combs=combinations(weight, i)
    #     for comb in combs: 
    #         print(list(comb), validate(comb), count(comb))
    #         if validate(comb):   
    #             return i  +1
    
tests = [
(    [1.01,1.01,1.01, 1.4, 2.4],3)
]
for test, expected in tests:
    results = efficientJanitor(test)
    print(results == expected, results)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     weight_count = int(input().strip())

#     weight = []

#     for _ in range(weight_count):
#         weight_item = float(input().strip())
#         weight.append(weight_item)

#     result = efficientJanitor(weight)

#     fptr.write(str(result) + '\n')

#     fptr.close()
