# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        tor = head
        har = head
        
        while tor and har and har.next:
            tor = tor.next
            har = har.next.next
            
            if tor == har:
                return True
        
        return False
        