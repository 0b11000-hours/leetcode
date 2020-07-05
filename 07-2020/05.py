# https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

def test_01():
    sol = Solution()
    assert sol.hammingDistance(1, 4) == 2

if __name__ == '__main__':
    test_01()
