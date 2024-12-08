# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        nth=head

        for i in range (0,n):
            nth=nth.next
        
        if(nth==None):
            return head.next
        
        while(nth.next!=None):
            nth=nth.next
            curr=curr.next

        curr.next=curr.next.next

        return head

        
