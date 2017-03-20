import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.floor(math.sqrt(area)))
        while w > 1:
            d = int(area % w)
            if d == 0:
                return [int(area/w), w]
            w -= 1
        return [area, w]
        
