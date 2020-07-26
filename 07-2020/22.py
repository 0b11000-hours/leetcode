# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _levelOrder(self, root, depth, result):
        if root == None:
            return result
        result = self._levelOrder(root.left, depth+1, result)
        while len(result) < depth+1:
            result.append([])
        result[depth].append(root.val)
        result = self._levelOrder(root.right, depth+1, result)
        return result

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = self._levelOrder(root, 0, [])
        for i in range(1, len(result), 2):
            result[i] = result[i][::-1]
        return result

