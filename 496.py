class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ans = []
        for f in findNums:
            found = False
            for i in range(nums.index(f), l):
                if f < nums[i]:
                    ans.append(nums[i])
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
        
