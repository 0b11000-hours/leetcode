# https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = i3 = i5 = 0
        ugly = [1]
        for i in xrange(n-1):
            next_num = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            if next_num == ugly[i2]*2: i2 += 1
            if next_num == ugly[i3]*3: i3 += 1
            if next_num == ugly[i5]*5: i5 += 1
            ugly.append(next_num)
        return ugly[n-1]

def test_01():
    sol = Solution()
    assert sol.nthUglyNumber(1) == 1
    assert sol.nthUglyNumber(10) == 12
    assert sol.nthUglyNumber(100) == 1536
    assert sol.nthUglyNumber(1690) == 2123366400

if __name__ == '__main__':
    test_01()
