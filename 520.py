class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        k = 0
        for ch in word:
            if ch.isupper():
                k += 1
        
        if k == 1 and word[0].isupper():
            return True
        
        if k == len(word):
            return True
        
        if k == 0:
            return True
        
        return False
        
