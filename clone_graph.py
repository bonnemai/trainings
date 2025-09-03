from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        results = f'Val: {self.val}'
        results += ' - '
        if self.neighbors is not None and len(self.neighbors)>0: 
            results += ' N: '
            for neighbor in self.neighbors: 
                results+=neighbor.__repr__()
        return results  

def copy_node(node:'Node')->'Node': 
    new_nodes=[]
    for neighbor in node.neighbors: 
        new_node=copy_node(neighbor)
        new_nodes.append(new_node)
    return Node(node.val, new_nodes)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: 
            return []
        return copy_node(node)
        # current_node=node
        # while current_node is not None: 
        #     node.neighbors

s=Solution()
print(s.cloneGraph(None))
print(s.cloneGraph(Node(1, [])))
print(s.cloneGraph(Node(1, [Node(2)])))
print(s.cloneGraph(Node(1, [Node(2, [Node(1),Node(3)]), Node(4, [Node(1), Node(3)])])))
