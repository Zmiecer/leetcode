class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def fizzBuzz(i, x):
            return {1: str(i), 3: "Fizz", 5: "Buzz", 15: "FizzBuzz"}[x]
        
        ans = []
        x = 1
        for i in range(1, n + 1):
            if i % 3 == 0:
                x *= 3
            if i % 5 == 0:
                x *= 5
            ans.append(fizzBuzz(i, x))
            x = 1
        return ans
        
