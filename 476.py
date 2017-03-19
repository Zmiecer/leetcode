class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def change(i):
            if i == '0':
                return '1'
            return '0'
        
        l = ''
        print(bin(num)[2:])
        for i in bin(num)[2:]:
            l += change(i)
        
        return int(l, 2)
        
