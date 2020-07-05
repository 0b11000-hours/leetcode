# https://leetcode.com/problems/ugly-number-ii/
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [(1, 0)]
        #ugly = [[(2, 0)], [(3, 1)], [(5, 2]]
        heapq.heapify(ugly)
        for i in xrange(n-1):
            (num, index) = heapq.heappop(ugly)
            if index == 0:
                heapq.heappush(ugly, (num*2, 0))
                heapq.heappush(ugly, (num*3, 1))
            elif index == 1:
                heapq.heappush(ugly, (num*3, 1))
            heapq.heappush(ugly, (num*5, 2))
        (num, index) = heapq.heappop(ugly)
        return num

def test_01():
    sol = Solution()
    assert sol.nthUglyNumber(1) == 1
    assert sol.nthUglyNumber(10) == 12

if __name__ == '__main__':
    test_01()
