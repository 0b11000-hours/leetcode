# https://leetcode.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i] == 2:
                del count[i]
        return count.keys()
