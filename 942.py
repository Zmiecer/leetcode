class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = 0
        r = len(S)
        ans = []
        for i in range(r):
            if S[i] == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        
        ans.append(l)
        return ans
