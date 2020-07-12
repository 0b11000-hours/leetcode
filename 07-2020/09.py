# https://leetcode.com/problems/maximum-width-of-binary-tree/ 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        res = 1
        queue = [[root, 0]]
        while len(queue) > 0:
            count = len(queue)
            start = queue[0][1]
            end = queue[-1][1]
            res = max(res, end - start + 1)
            for i in range(count):
                ele = queue[0]
                idx = ele[1] - start
                queue.pop(0)
                if ele[0].left != None: queue.append([ele[0].left, 2*idx+1])
                if ele[0].right != None: queue.append([ele[0].right, 2*idx+2])
        return res

def test_01():
    sol = Solution()
    assert sol.widthOfBinaryTree(TreeNode(1, TreeNode(2))) == 1
    assert sol.widthOfBinaryTree(TreeNode(1)) == 1
    t = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert sol.widthOfBinaryTree(t) == 4
    t = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(2)))
    assert sol.widthOfBinaryTree(t) == 2
    t = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    assert sol.widthOfBinaryTree(t) == 2
    t = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, None, TreeNode(7))))
    assert sol.widthOfBinaryTree(t) == 8

if __name__ == '__main__':
    test_01()
