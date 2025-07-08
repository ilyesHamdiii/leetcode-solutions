# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Difficulty: Medium


# Time: O(n)
# Space: O(n)












class Solution(object):
    def deleteMiddle(self, head):
        itr=head
        x=0
        while itr:
            x+=1
            itr=itr.next
        i=0
        itr=head
        prev=head
        if(x==1):
            head =None
            return head
        if(head is None ):
            return head


        while i<x/2:
            prev=itr
            i+=1
            itr=itr.next
        prev.next=itr.next
        return head

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
