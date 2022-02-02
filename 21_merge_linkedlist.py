# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        ans = curr
        
        a = list1
        b = list2
        
        while a is not None and b is not None:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            
            curr = curr.next
        
        while a is not None:
            curr.next = a
            a = a.next
            curr = curr.next
        
        while b is not None:
            curr.next = b
            b = b.next
            curr = curr.next
        
        return ans.next
            
        