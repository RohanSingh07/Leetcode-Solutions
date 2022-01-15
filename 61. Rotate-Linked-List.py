# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Faster than 60% ___

# Approach:_____
# Use Two pointers to find the (k-1)th element from the last 
# make the kth element the head and (k-1)th element point to None
# Tranverse to the end of the new head and make the last element point to the previous head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k==0: # Exceptions
            return head
        
        length = 1
        ptr = head
        while ptr.next!=None:
            length+=1
            ptr = ptr.next
        
        k = k%length
        
        if length ==1 or k==0: # Expections indicating no more further modification is needed in LL
            return head 
        
        ptr1 = head
        ptr2 = head
        t = k
        while t:
            ptr2 = ptr2.next
            t-=1
        while ptr2.next!=None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        t = head
        head = ptr1.next
        ptr1.next = None
        ptr1 = head
        while ptr1.next !=None:
            ptr1 = ptr1.next
        ptr1.next = t
        return head
