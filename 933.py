class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1
        while l != r:
            m = (l + r) // 2
            if A[m - 1] > A[m]:
                r = m
            elif A[m] < A[m + 1]:
                l = m
            else:
                return m
