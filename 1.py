class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        
        for i in range(len(nums)):
            try:
                dict[target - nums[i]].append(i)
            except:
                dict[target - nums[i]] = [i]
            try:
                if dict[nums[i]] != [-1]:
                    for j in range(len(dict[nums[i]])):
                        if dict[nums[i]][j] != i:
                            return [dict[nums[i]][j], i]
            except Exception:
                continue
                
