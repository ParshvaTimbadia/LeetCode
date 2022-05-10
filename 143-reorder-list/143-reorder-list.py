# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def getMid(head):
            
            previous = None
            slow = head
            fast = head
            
            while fast is not None and fast.next is not None:
                previous = slow
                slow = slow.next
                fast = fast.next.next
            
            return slow, previous
        
        def reverseLinkedList(head):
            
            previous = None
            curr = head
            while curr != None:
                nextNode = curr.next
                curr.next = previous
                previous = curr
                curr = nextNode
            
            return previous
        
        mid, previous_mid = getMid(head)
        if previous_mid is None:
            return head
        previous_mid.next = None
        new_head = reverseLinkedList(mid)
        
        
        
        curr = head
        first = True
        result = head
        
        while head is not None and new_head is not None:
            
            if first:
                head = head.next
                curr.next = new_head
            else:
                new_head = new_head.next
                curr.next = head
            
            first = not first
            curr = curr.next
        
        return result
                
            
            
            
            
            