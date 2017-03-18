class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        prev = nums[0]
        k = 1
        i = 0
        while(True):
            i += 1
            if i==len(nums):
                break
            if nums[i] != prev:
                k += 1
                prev = nums[i]
            else:
                nums.pop(i)
                i -= 1
        return k
        
