# https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, list(str(int("".join(map(str, digits))) + 1)))

def test_01():
    sol = Solution()
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert sol.plusOne([0]) == [1]
    assert sol.plusOne([9 , 9]) == [1, 0, 0]

if __name__ == '__main__':
    test_01()
