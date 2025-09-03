from copy import copy,deepcopy

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value=value
        self.next=next
    
    def __str__(self) -> str:
        current = self
        results=''
        while current:
            results+=str(current.value)+ ' '
            current=current.next
        return results
        

l=ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(l)
print(copy(l))
print(deepcopy(l))