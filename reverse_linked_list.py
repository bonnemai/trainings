
class Node:
    def __init__(self, value: int, next=None) -> None:
        self.value=value
        self.next=next

root=Node(1, Node(2, Node(3, Node(4))))
def reverse(root:Node): 
    prev=None
    current=root
    next=None
    while current is not None: 
        next=current.next
        current.next=prev
        prev=current
        current=next
    return prev

def print_linked_list(root:Node): 
    current=root
    while current is not None: 
        print(current.value)
        current=current.next
print_linked_list(root)
print ('++++++++++++')
print_linked_list(reverse(root))