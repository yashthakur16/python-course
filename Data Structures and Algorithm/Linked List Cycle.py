# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None or head.next==None):
            return False
        
        slow=head.next
        fast=head.next.next

        while(slow!=fast and fast !=None and fast.next !=None):
            slow=slow.next
            fast=fast.next.next

        if(fast==None or fast.next==None):
            return False

        return True
        
