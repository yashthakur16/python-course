# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,head):
        if(head==None or head.next==None):
            return head
        
        curr=head
        prev=None
        forward=head.next

        while(curr.next!=None):
            curr.next=prev
            prev=curr
            curr=forward
            forward=forward.next
        
        curr.next=prev
        prev=curr
        curr=forward

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while(slow !=None and fast !=None):
            slow=slow.next
            fast=fast.next
            if(fast!=None):
                fast=fast.next

        l2=self.reverse(slow)
        l1=head

        while(l1!=None and l2!=None):
            if(l1.val!=l2.val):
                return False
            l1=l1.next
            l2=l2.next

        return True
        
