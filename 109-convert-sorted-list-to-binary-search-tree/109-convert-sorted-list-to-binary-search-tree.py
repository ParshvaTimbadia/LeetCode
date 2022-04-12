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
        
        slow = head
        fast = head
        slowPrevious = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slowPrevious = slow
            slow = slow.next
        
        return slow, slowPrevious
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head is None:
            return None
        
        if head and head.next is None:
            return TreeNode(head.val)
        
        mid, midPrevious = self.findMid(head)

        righthead = mid.next
        if midPrevious:
            midPrevious.next = None
            
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(righthead)
        
        return node
        
        