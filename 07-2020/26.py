# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        res = 0
        while(num):
            res += num % 10
            if res > 9:
                res = 1 + res % 10
            num /= 10
        return res

def test_01():
    sol = Solution()
    assert sol.addDigits(38) == 2
    assert sol.addDigits(39) == 3
    assert sol.addDigits(40) == 4
    assert sol.addDigits(19) == 1

if __name__ == '__main__':
    test_01()
