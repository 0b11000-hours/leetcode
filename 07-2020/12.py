# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin, 2)

def test_01():
    sol = Solution()
    assert sol.reverseBits(43261596) == 964176192
    assert sol.reverseBits(4294967293) == 3221225471

if __name__ == '__main__':
    test_01()
