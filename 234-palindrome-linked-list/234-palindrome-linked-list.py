# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
    
        middleNode = self.getMiddleList(head)
        new_head = self.reverseLinkedList(middleNode)
        
        while head and new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        
        return True
    
    
    
    
    def getMiddleList(self, node):
        
        slow, fast = node, node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseLinkedList(self, node):
        previous = None
        while node is not None:
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
        return previous