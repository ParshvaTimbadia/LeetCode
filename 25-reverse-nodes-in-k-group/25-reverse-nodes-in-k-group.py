# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head, end):
        curr = head
        previous = None
        while curr is not None and curr != end:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
        
        return previous, curr
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        newHead = ListNode()
        previous = newHead
        curr = head
        
        while curr is not None:
            
            start, end = curr, curr
            i = 1
            while end is not None and i < k:
                end = end.next
                i += 1

            if end == None:
                break
                
            node_before_reversal = previous
            last_node_to_be = start
            
            reversed_head, next_node = self.reverseList(start, end.next)
            node_before_reversal.next = reversed_head
            last_node_to_be.next = next_node
            
            curr = next_node
            previous = last_node_to_be
        
        return newHead.next

            