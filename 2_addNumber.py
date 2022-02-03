# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0
        
        while l1 or l2:
            sum = carry
            
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry = sum//10
            value = sum % 10
            
            curr.next = ListNode(value)
            curr = curr.next
        
        if carry == 1 :
            curr.next = ListNode(carry)
        
        return head.next