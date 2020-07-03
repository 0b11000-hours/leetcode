# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        if root is None:
            return res
        node_list = [root]
        while node_list:
            res.append([i.val for i in node_list])
            new_nodes_list = [j for i in node_list for j in (i.left, i.right) if j is not None]
            node_list = new_nodes_list
        return list(reversed(res))

def test_01():
    sol = Solution()
    assert sol.levelOrderBottom(1) == 1

if __name__ == '__main__':
    test_01()
