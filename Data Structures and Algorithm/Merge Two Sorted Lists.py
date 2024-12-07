# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1==None and list2==None):
            return None
        
        if(list1==None):
            return list2
        
        if (list2==None):
            return list1

        head=list1
        ans=list1

        if(list1.val<list2.val):
            head=list1
            ans=list1
            list1=list1.next
        else:
            head=list2
            ans=list2
            list2=list2.next
        
        l1=list1
        l2=list2

        while(l1!=None and l2!=None):
            if(l1.val<l2.val):
                head.next=l1
                head=head.next
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
                head=head.next

        while(l1!=None):
            head.next=l1
            head=head.next
            l1=l1.next

        while(l2!=None):
            head.next=l2
            l2=l2.next
            head=head.next

        return ans

        



