# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
        results=[]
        while current1 is not None or current2 is not None: 
            if current1 is not None and current1.val<=current2.val:
                results.append(current1.val)
                current1=current1.next
            elif current2 is not None:
                results.append(current2.val)
                current2=current2.next
        return from_list(results)

def print_linked_list(node:ListNode): 
    current=node
    while current: 
        print(current.val,  end='')
        current=current.next
        if current is not None: 
                print( '-> ', end='')

    print ('')

def from_list(lst:[]): 
    results=None
    while len(lst)>0: 
        results=ListNode(lst.pop(), results)
    return results

listNode1=ListNode(1, ListNode(2))
listNode2=ListNode(1, ListNode(3))

# print_linked_list(listNode1)
print_linked_list(Solution().mergeTwoLists(listNode1, listNode2))
# print_linked_list(from_list([1,2,3,4,5,6]))