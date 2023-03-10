class Solution:
    def isValid(self, s: str) -> bool:
        pair_to_closeds = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for bracket in s:
            if bracket not in pair_to_closeds:
                stack.append(bracket)
                continue
            if len(stack) == 0 or stack[-1] != pair_to_closeds[bracket]:
                return False
            stack.pop()
        return len(stack) == 0
