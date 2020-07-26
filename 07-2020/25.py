# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution(object):
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            start, end = 0, len(nums) - 1
            while (start < end):
                mid = (start + end) / 2
                if nums[mid] < nums[end]:
                    end = mid
                elif nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end -= 1
            return nums[start]

def test_01():
    sol = Solution()
    assert sol.findMin([1, 3, 5]) == 1
    assert sol.findMin([2, 2, 2, 0, 1]) == 0
    assert sol.findMin([2, 2, 2, 2, 2]) == 2
    assert sol.findMin([3, 1, 1]) == 1
    assert sol.findMin([3, 3, 1, 3]) == 1

if __name__ == '__main__':
    test_01()
