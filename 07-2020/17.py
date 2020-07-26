# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        items = [(-value, key) for key, value in count.items()]
        smallest = heapq.nsmallest(k, items)
        result = [key for value, key in smallest]
        return result
