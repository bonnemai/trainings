#!/bin/python3

from asyncio import constants
import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def sum_line(s, i):
    l1=s[0][i]+s[1][i]+s[2][i]
    return l1

def sum_col(s, i):
    c1=s[i][0]+s[i][1]+s[i][2]
    return c1


def formingMagicSquare(s):
    # Write your code here
    sums=[]
    c1=s[0][0]+s[0][1]+s[0][2]
    c2=s[1][0]+s[1][1]+s[1][2]
    c3=s[2][0]+s[2][1]+s[2][2]

    l1=s[0][0]+s[1][0]+s[2][0]
    l2=s[1][1]+s[1][1]+s[1][1]
    l3=s[2][2]+s[2][2]+s[2][2]
    
    d1=s[0][0]+s[1][1]+s[2][2]
    d2=s[0][2]+s[1][1]+s[2][0]
    sums=[c1,c2,c3,l1,l2,l3,d1,d2]
    _map={}
    for sum_1 in sums:
        if sum_1 in _map:
            _map[sum_1]+=1
        else:
            _map[sum_1]=1    
    print(_map)
    magic_number_count=max(_map.values())
    for k, v in _map.items():
        if v==magic_number_count:
            magic_number=k
    print(magic_number)
    # suspicious_i=-1
    # suspicious_j=-1
    change=0
    for i in range(3):
        if sum_col(s, i)!=magic_number:
            print('suspicious col: ', i)
            suspicious_i=i
        if sum_line(s,i)!=magic_number:
            print('suspicious line: ', i)
            suspicious_j=i
        print(suspicious_i, suspicious_j)
        change+=math.fabs(sum_line(s,i)-magic_number)
    print (change)    
    return change
    # for i in range(3): 
    #     for j in range(3):
    #        s[i][j] 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # 4 8 2
    # 4 5 7
    # 6 1 6
    matrix1=[[4 ,8, 2],[4, 5, 7],[6, 1, 6]]
    # matrix=[[4, 9, 2],[3, 5, 7],[8, 1, 5]]
    #matrix=[[4, 9, 2],[3, 5, 7],[8, 1, 6]]

    # s = []
    results1 = formingMagicSquare(matrix1)
    print("1:", results1, "Expected: ", 4)
    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
