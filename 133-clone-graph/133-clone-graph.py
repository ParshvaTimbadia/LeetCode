"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        seen = {}
        def helper(node):
            
            if node is None:
                return None
            
            if node in seen:
                return seen[node]
            
            seen[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                seen[node].neighbors.append(helper(neighbor))
            
            return seen[node]
        
        return helper(node)
        
                