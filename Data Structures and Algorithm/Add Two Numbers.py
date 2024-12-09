# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        curr=head
        carry=0

        while(l1!=None and l2!=None):
            add=l1.val+l2.val+carry
            node=ListNode(val=add%10)
            curr.next=node
            curr=curr.next
            carry=add//10
            l1=l1.next
            l2=l2.next
        
        while(l1!=None):
            add=l1.val+carry
            node=ListNode(val=add%10)
            curr.next=node
            curr=curr.next
            carry=add//10
            l1=l1.next
        
        while(l2!=None):
            add=l2.val+carry
            node=ListNode(val=add%10)
            curr.next=node
            curr=curr.next
            carry=add//10
            l2=l2.next

        if(carry !=0):
            add=carry
            node=ListNode(val=add%10)
            curr.next=node
            curr=curr.next

        return head.next
            


        
