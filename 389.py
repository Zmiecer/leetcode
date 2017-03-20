class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        for i in range(len(t)):
            try:
                s.pop(s.index(t[i]))
            except ValueError:
                return t[i]
