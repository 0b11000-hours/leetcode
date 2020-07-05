# https://leetcode.com/problems/prison-cells-after-n-days/
import sys
import pprint
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def cal_next(start):
            new_list = [0] * 8
            for i in range(1, len(start)-1):
                new_list[i] = 1-(start[i-1]^start[i+1])
            new_list[0] = new_list[-1] = 0
            return new_list

        def to_num(start):
            res = 0
            w = 1
            for i in start:
                res += w*i
                w *= 2
            return res
        def to_list(num):
            res = [0] * 8
            i = 0
            while num:
                res[i] = num % 2
                num /= 2
                i += 1
            return res

        mapping = {}
        start = to_num(cells)
        for i in xrange(256):
            mapping[i] = to_num(cal_next(to_list(i)))
        for i in xrange(N % 14 + 14):
            start = mapping[start]
        return to_list(start)

def test_01():
    sol = Solution()
    assert sol.prisonAfterNDays([1,0,0,1,0,0,0,1], 826) == [0,1,1,0,1,1,1,0]
    assert sol.prisonAfterNDays([0,1,0,1,1,0,0,1], 7) == [0,0,1,1,0,0,0,0]
    assert sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) == [0,0,1,1,1,1,1,0]

if __name__ == '__main__':
    test_01()
