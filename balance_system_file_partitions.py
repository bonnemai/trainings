#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#
from collections import deque
class Node:
     def __init__(self, data):
         self.children = []
         self.data = data
         self.total=0



def mostBalancedPartition(parent, files_size):
    # Write your code here
    # for parent, files_size in zip(parent, files_size): 
    _map={}
    for i in range(len(files_size)): 
        _map[i]=Node(files_size[i])
    for i in range(len(parent)): 
        if parent[i]!=-1: 
            _map[i].children.append(_map[parent[i]])
    list_of_branches_sum=[]
    _sum=0
    pre_order(_map[0], _sum)
    # queue=deque(0)
    # visited=[False]*len(parent)
    # total=[0]*len(parent)
    # while queue: 
    #     current_node=queue.popleft()
    #     for i in parent: 
    #         if parent[i]==current_node and not visited[i]:
    #             queue.append(i)
    #         total[i]


def pre_order(root,_sum):
   list_of_branches_sum=[]
   if root:
        _sum = _sum + root.data
        for child in root.children: 
            a = pre_order(child, _sum)
        # b = pre_order(root.right, sum)


        if (len(root.children)==0):
            list_of_branches_sum.append(_sum)

   return list_of_branches_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()
