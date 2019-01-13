class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """        
        return ''.join(map(lambda ch: chr(ord(ch) + 32) if 64 < ord(ch) < 91 else ch, str))
        # return str.lower()
    
