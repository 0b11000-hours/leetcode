# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        res = ((hour % 12) * 30 + minutes / 2.0) - minutes * 6
        if res < 0:
            res = -res
        if res > 180:
            res = 360 - res
        print(res)
        return res

def test_01():
    sol = Solution()
    assert sol.angleClock(12, 30) == 165
    assert sol.angleClock(3, 30) == 75
    assert sol.angleClock(3, 15) == 7.5
    assert sol.angleClock(4, 50) == 155
    assert sol.angleClock(12, 0) == 0
    assert sol.angleClock(6, 0) == 180
    assert sol.angleClock(1, 57) == 76.5
    assert sol.angleClock(12, 45) == 112.5

if __name__ == '__main__':
    test_01()
