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
        
        hMap = {}
        curr = head
        while curr:
            hMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            hMap[curr].next = hMap[curr.next] if curr.next else None
            hMap[curr].random = hMap[curr.random] if curr.random else None
            curr = curr.next
        
        return hMap[head]
        
        