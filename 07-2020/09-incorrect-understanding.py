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
        # (width, lpath, rpath)
        def widthTree(root):
            if root.left == None and root.right == None:
                return (0, 0, 0)
            w = l = r = 0
            if root.left:
                left = widthTree(root.left)
                l = left[1] + 1
            else:
                left = (0, 0, 0)
            if root.right:
                right = widthTree(root.right)
                r = right[2] + 1
            else:
                right = (0, 0, 0)
            print(root.val, "left",  left)
            print(root.val, "right", right)
            w = max(left[0], right[0])
            if l != 0 and r != 0 :
                w = max(w, min(l, r))
            #if left[1] == right[2] and left[1] != 0:
                #w = max(w, min(left[1]+1, right[2]+1))
            #w = max(w, min(left[1], right[2]))
            print(root.val, w, l, r)
            return (w, l, r)
        res = widthTree(root)
        power = max(res[0], min(res[1], res[2]))
        print(res)
        return 2**power

def test_01():
    sol = Solution()
    assert sol.widthOfBinaryTree(TreeNode(1, TreeNode(2))) == 1
    assert sol.widthOfBinaryTree(TreeNode(1)) == 1
    t = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert sol.widthOfBinaryTree(t) == 4
    t = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(2)))
    assert sol.widthOfBinaryTree(t) == 2
    print("1")
    t = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    assert sol.widthOfBinaryTree(t) == 2
    t = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, None, TreeNode(7))))
    assert sol.widthOfBinaryTree(t) == 8

if __name__ == '__main__':
    test_01()
