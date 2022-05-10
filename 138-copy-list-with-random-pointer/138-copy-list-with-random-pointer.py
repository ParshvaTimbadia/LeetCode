"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return 
        
        store = {}
        curr = head
        while curr is not None:
            store[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr is not None:
            new_node = store[curr]
            new_node.next = store[curr.next] if curr.next else None
            new_node.random = store[curr.random] if curr.random else None
            curr = curr.next
        
        return store[head]
            