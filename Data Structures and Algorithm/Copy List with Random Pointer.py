"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if(head==None):
            return head
            
        curr=head
        temp=Node(x=0)

        while(curr!=None):
            node=Node(curr.val)
            node.next=curr.next
            curr.next=node
            curr=node.next

        curr=head

        while(curr!=None):
            if (curr.random==None):
                curr.next.random=None
            else:
                curr.next.random=curr.random.next
            
            curr=curr.next
            if(curr!=None):
                curr=curr.next

        
        curr=head
        curr2=head.next
        temp.next=curr2

        while(curr2.next!=None):
            curr2.next=curr2.next.next
            curr2=curr2.next

        return temp.next

