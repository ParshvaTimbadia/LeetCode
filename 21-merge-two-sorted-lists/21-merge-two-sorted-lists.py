# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
  
        curr = ListNode()
        result = curr
        pointer1 = list1
        pointer2 = list2
        
        while pointer1 is not None and pointer2 is not None:
            
            if pointer1.val <= pointer2.val:
                curr.next = pointer1
                pointer1 = pointer1.next
            else:
                curr.next = pointer2
                pointer2 = pointer2.next
            curr = curr.next
        
        if pointer1 is not None:
            curr.next = pointer1
        
        if pointer2 is not None:
            curr.next = pointer2
        
        return result.next
                
                