class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxlength=0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlength=max(maxlength,i-stack[-1])
        return maxlength