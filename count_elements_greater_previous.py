#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    _sum=0
    results=0
    for i in range(len(responseTimes)): 
        if i>0: 
            if responseTimes[i]>(_sum/i): 
                results+=1
        _sum+=responseTimes[i]
    return results

if __name__ == '__main__':
    # responseTimes_count = int(input().strip())

    # responseTimes = []

    # for _ in range(responseTimes_count):
    #     responseTimes_item = int(input().strip())
    #     responseTimes.append(responseTimes_item)
    responseTimes=[100, 200, 150, 300]
    result = countResponseTimeRegressions(responseTimes)

    print(result)
