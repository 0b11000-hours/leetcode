# https://leetcode.com/problems/subsets/

class Solution(object):
        def subsets(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            if len(nums) == 0:
                return [[]]
            else:
                s1 = self.subsets(nums[1:])
                return [item + [nums[0]] for item in s1] + s1

def test_01():
    sol = Solution()
    print(sol.subsets([]))
    print(sol.subsets([1]))
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([1, 2, 3, 4]))

if __name__ == '__main__':
    test_01()
