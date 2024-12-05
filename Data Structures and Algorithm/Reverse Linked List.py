# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        
        curr=head
        prev=None
        forward=head.next

        while(curr.next !=None):
            curr.next=prev
            prev=curr
            curr=forward
            forward=curr.next
        
        curr.next=prev
        prev=curr
        
        return prev
        
