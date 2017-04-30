class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        kek = []
        nums = [item for sublist in nums for item in sublist]
        k = 0
        for i in range(r):
            kek.append([])
            for j in range(c):
                kek[i].append(nums[i*c + j])
        return kek
