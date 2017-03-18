class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = list(bin(x)[2:]), list(bin(y)[2:])
        s1 = list('0' * max(len(x), len(y)))
        s2 = list('0' * max(len(x), len(y)))
        s1[len(s1) - len(x):] = x
        s2[len(s2) - len(y):] = y
        k = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                k += 1
        return k
        
