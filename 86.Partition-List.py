# Two pointer solution
# Take two dummy nodes
# One will point to all the nodes less than x
# One will point to all the nodes greater than x
# Join them 

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:  
        if head == None or head.next == None:
            return head
        head1 = ListNode(0)
        head2= ListNode(0)
        ptr1 = head1
        ptr2 = head2
        temp = head
        while temp!=None:
            if temp.val<x:
                ptr1.next = temp
                ptr1 = ptr1.next
            else:
                ptr2.next = temp
                ptr2 = ptr2.next    
            temp = temp.next
        ptr1.next = head2.next
        ptr2.next = None
        return head1.next
