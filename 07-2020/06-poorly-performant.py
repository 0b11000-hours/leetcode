# https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 0
        digits[-1] += 1
        for i in reversed(digits):
            res.append((carry + i)%10)
            carry = (carry + i) /10
        if carry == 1:
            res.append(1)
        return list(reversed(res))

def test_01():
    sol = Solution()
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert sol.plusOne([0]) == [1]
    assert sol.plusOne([9 , 9]) == [1, 0, 0]

if __name__ == '__main__':
    test_01()
