class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        l = len(nums)
        for i in range(l):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        nums[count:l] = [0] * (l - count)
        
