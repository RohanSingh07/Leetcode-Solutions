# Two pointer logic
# When we find a dublicate ptr.val == ptr.next.val we will move ptr until different value is found
# then pptr.next = ptr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pptr = head
        ptr = head
        while ptr.next != None:
            if ptr.val == ptr.next.val:
                val = ptr.val
                while ptr.val == val:
                    ptr = ptr.next
                    if ptr == None:
                        break
                if ptr == None and head.val == val:
                    return None
                elif head == pptr and pptr.val == val:
                    head = ptr
                    pptr = head
                else:
                    pptr.next = ptr
                    if ptr == None:
                        break      
            else:
                pptr = ptr
                ptr = ptr.next
        return head
