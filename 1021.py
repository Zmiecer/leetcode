class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        answer = []
        brackets = 0
        prev_index = 0
        for index, ch in enumerate(S):
            if ch == '(':
                brackets += 1
            else:
                brackets -= 1
            if brackets == 0:
                answer.append(S[prev_index + 1:index])
                prev_index = index + 1
        return ''.join(answer)
