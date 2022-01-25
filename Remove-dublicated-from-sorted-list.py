# Single pass, O(n),O(1) Solution
# When we find two adjacent nodes with same value, we take a new pointer which points to the first repeating element
# Then it will proceed further till it finds a node with different value
# Then we can make ptr1 point directly to that node and continue like this till end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        ptr1 = head
        while ptr1.next!=None:
            if ptr1.next.val!=ptr1.val:
                ptr1 = ptr1.next
            else:
                ptr2 = ptr1
                while ptr2.val == ptr1.val:
                    ptr2 = ptr2.next
                    if ptr2 == None:
                        break
                ptr1.next = ptr2
                ptr1 = ptr1
        return head
