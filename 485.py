class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        k = 0
        for i in nums:
            if i == 1:
                k += 1
            else:
                if k > m:
                    m = k
                k = 0
        if k > m:
            m = k
        return m
