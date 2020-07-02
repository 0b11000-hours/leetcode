class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = int((((1+8*n)**0.5)-1)/2)
        return res

def test_01():
    sol = Solution()
    assert sol.arrangeCoins(1) == 1
    assert sol.arrangeCoins(3) == 2
    assert sol.arrangeCoins(5) == 2
    assert sol.arrangeCoins(6) == 3
    assert sol.arrangeCoins(8) == 3
    assert sol.arrangeCoins(54) == 9
    assert sol.arrangeCoins(55) == 10
    assert sol.arrangeCoins(56) == 10

if __name__ == '__main__':
    test_01()
