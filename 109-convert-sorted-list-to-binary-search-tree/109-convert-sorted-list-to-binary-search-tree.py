# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMid(self, head):
        
        firstNode = None
        slow = head
        fast = head
        slowPrevious = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slowPrevious = slow
            if not firstNode:
                firstNode = slow
            slow = slow.next
        
        return firstNode, slow, slowPrevious
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head is None:
            return None
        
        start, mid, midPrevious = self.findMid(head)
        
        node = TreeNode(mid.val)
        
        lefthead = start
        righthead = mid.next
        if midPrevious:
            midPrevious.next = None
        
        node.left = self.sortedListToBST(lefthead)
        node.right = self.sortedListToBST(righthead)
        
        return node
        
        