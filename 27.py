class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while True:
            if i >= len(nums):
                break
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return i
        
