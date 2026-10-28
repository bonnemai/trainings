#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#
# TODO: Palindrome on LinkedList. 
def isAlphabeticPalindrome(code):
    # Write your code here
    code=code.lower()
    new_code=""
    for c in code: 
        if c.isalpha(): 
            new_code=new_code+c
    for i in range(0, len(new_code)//2):
        if new_code[i]!=new_code[len(new_code)-1-i]: 
            return False
    return True

class Node: 
    def __init__(self, value) -> None:
        self.value=value
        self.next=None
    
    
def is_palindrome_linked_list(element:Node):
    while element.next and element.next.next: 
        slow=element.next
        fast=element.next.next

if __name__ == '__main__':
    code = "abcb!!!a" #input()
    result = isAlphabeticPalindrome(code)
    print(result)
