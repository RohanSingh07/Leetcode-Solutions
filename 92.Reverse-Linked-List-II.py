# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Straight forward two pointer solution

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next ==None:
            return head
        
        lptr = head
        c = left
        while c>1:
            
            lptr = lptr.next
            c-=1
            
        c = right
        rptr = head
        while c>1:
            rptr = rptr.next
            c-=1
        
        ptr1 = lptr
        ptr2 = lptr.next
        while ptr2!=None and ptr1 != rptr:
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = temp
        lptr.next = ptr2
        if lptr == head:
            head = rptr
        else:
            m = head
            while m.next!=lptr:
                m = m.next
            m.next = rptr
        return head
