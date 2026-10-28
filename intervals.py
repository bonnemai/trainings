#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    intervals=sorted(intervals, key=lambda x:x[0], reverse=False)
    if len(intervals)==0:
        return []

    merged_list=[intervals[0]]
    for i in range(len(intervals)):
        current = merged_list[-1]
        if current[1]<intervals[i][0]: 
            merged_list.append(intervals[i])
        else:
            end=max(current[1], intervals[i][1])
            current[1]=end
            # merged_list.append([current[0], end])
        # prev=intervals[i]
        # if  intervals[i+1][1]>intervals[i][1]: 
        #     merged_list[i]=[intervals[intervals[i][0]], intervals[intervals[i+1][1]]]
    # TODO: last
    return merged_list

if __name__ == '__main__':
    # intervals_rows = int(input().strip())
    # intervals_columns = int(input().strip())

    # intervals = []

    # for _ in range(intervals_rows):
    #     intervals.append(list(map(int, input().rstrip().split())))
    intervals = [[1,3], [2,6], [7,8]]
    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
