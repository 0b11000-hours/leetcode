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
        def traverse(node_list, res):
            values = [i.val for i in node_list]
            new_nodes_list = [j for i in node_list for j in (i.left, i.right) if j is not None]
            res.append(values)
            if new_nodes_list:
                traverse(new_nodes_list, res)

        res = []
        if root is None:
            return res
        traverse([root], res)
        return res[::-1]

def test_01():
    sol = Solution()
    assert sol.levelOrderBottom(1) == 1

if __name__ == '__main__':
    test_01()
