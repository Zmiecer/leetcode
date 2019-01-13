class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        hor = 0
        ver = 0
        moveset = {'R': 1, 'L': -1, 'U': 1000, 'D': -1000}
        map(lambda move: moveset[move], moves)
        for move in moves:
            if move == 'R':
                hor += 1
            elif move == 'L':
                hor -= 1
            elif move == 'U':
                ver += 1
            elif move == 'D':
                ver -= 1
        
        return hor == ver == 0
