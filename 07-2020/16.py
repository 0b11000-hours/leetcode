# https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1/self.myPow(x, -n)
        if n % 2 == 0:
            p = self.myPow(x, n//2)
            return p*p
        else:
            p = self.myPow(x, (n-1)/2)
            return x*p*p
