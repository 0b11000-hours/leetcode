# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def iflatten(head):
            start = snext = head
            while snext != None:
                start = snext
                snext = snext.next
                if start.child != None:
                    last = iflatten(start.child)
                    if start.next:
                        last.next = start.next
                        start.next.perv = last
                    start.next = start.child
                    start.child = None
                    start.next.prev = start
            return start
        iflatten(head)
        return head

def test_01():
    sol = Solution()

if __name__ == '__main__':
    test_01()
