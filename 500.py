class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        def inOneRow(word):
            mask = [0, 0, 0]
            for i in range(len(rows)):
                for ch in word:
                    if ch in rows[i]:
                        mask[i] = 1
            return sum(mask) == 1
        
        ans = []
        for word in words:
            wordl = word.lower()
            if inOneRow(wordl):
                ans.append(word)
        return ans
        
