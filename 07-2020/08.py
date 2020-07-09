# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i1, num1 in enumerate(nums):
            if i1 > 0 and nums[i1] == nums[i1-1]: continue
            i2 = i1+1
            i3 = len(nums)-1
            while(i2 < i3):
                r1 = nums[i1] + nums[i2] + nums[i3]
                if r1 == 0:
                    l1 = [nums[i1], nums[i2], nums[i3]]
                    if len(res) > 0 and res[-1] == l1:
                        i2 += 1
                        i3 -= 1
                        continue
                    res.append(l1)
                if r1 < 0: i2 += 1
                else: i3 -= 1
        return res
def test_01():
    sol = Solution()
    assert sol.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

if __name__ == '__main__':
    test_01()
