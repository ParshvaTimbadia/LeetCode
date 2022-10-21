# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        head = ListNode()
        curr = head
        carry = 0
        node1, node2 = l1, l2
        
        while node1 or node2:
            
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            
            totalSum = (val1 + val2 + carry)%10
            carry = (val1 + val2 + carry)//10
            
            curr.next = ListNode(totalSum)
            curr = curr.next
             
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return head.next