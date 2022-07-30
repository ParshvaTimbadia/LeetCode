# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []
        newHead = ListNode()
        pointer = newHead
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(minHeap, (lists[i].val, i, lists[i]))
        
        
        while minHeap:
            
            value,i, head = heappop(minHeap)
            
            pointer.next = ListNode(value)
            
            if head.next:
                heappush(minHeap, (head.next.val, i,head.next))
            
            pointer = pointer.next
        
        return newHead.next