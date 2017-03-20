class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def reverse_numeric(x, y):
            return y - x
        kek = sorted(nums, cmp=reverse_numeric)
        l = len(nums)
        if l > 0:
            nums[nums.index(kek[0])] = "Gold Medal"
        if l > 1:
            nums[nums.index(kek[1])] = "Silver Medal"
        if l > 2:
            nums[nums.index(kek[2])] = "Bronze Medal"
        if l > 3:
            for i in range(3, l):
                nums[nums.index(kek[i])] = str(i + 1)
        return nums
        
