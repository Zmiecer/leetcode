class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        unique = set()
        for val in A:
            if val not in unique:
                unique.add(val)
            else:
                return val
