class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for row in A:
            B.append(list(reversed(row)))
        
        for i in range(len(B)):
            for j in range(len(B[0])):
                B[i][j] = B[i][j] ^ 1
        return B
