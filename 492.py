class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while w > 1:
            if area % w == 0:
                return [int(area/w), w]
            w -= 1
        return [area, 1]
        
