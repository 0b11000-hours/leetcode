# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        start = head
        while start and start.next != None:
            if start.next.val == val:
                tmp = start.next.next
                start.next = tmp
            else :
                tmp = start.next
                start = tmp
        return head
        
