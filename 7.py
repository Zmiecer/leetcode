class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        s = str(x)[::-1]
        x = int(s)
        if x > 2147483647:
            return 0
        return x * sign
