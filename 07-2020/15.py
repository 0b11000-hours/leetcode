# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])

def test_01():
    sol = Solution()
    assert sol.reverseWords("the sky is blue") == "blue is sky the"
    assert sol.reverseWords("  hello world!  ") == "world! hello"
    assert sol.reverseWords("a good   example") == "example good a"

if __name__ == '__main__':
    test_01()
