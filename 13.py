class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = nums[s[0]]
        for i in range(1, len(s)):
            if nums[s[i]] > nums[s[i-1]]:
                sum -= 2 * nums[s[i-1]]
            sum += nums[s[i]]
        return sum
        
