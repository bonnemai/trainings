# Definition for singly-linked list.
from typing import Optional
from copy import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head:ListNode):
    current=head
    prev=None
    # next=None
    while current is not None:
        next=current.next
        current.next=prev
        prev=current
        current=next

    return prev

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None: 
            return True
        if head.next is None: 
            return True
        current=copy(head)
        reversed=copy(reverseLinkedList(copy(head)))
        
        while current is not None: # and reversed is not None:
            if current.val!=reversed.val: 
                return False
            current=current.next
            reversed=reversed.next
        return True
head1=ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
head2=ListNode(1, ListNode(1, ListNode(2, ListNode(1))))

tests=[
    # (head2, False),
    (head1, True)
    ]
for (head, expected_results) in tests:
    res=Solution().isPalindrome(head)
    print(res==expected_results, res)