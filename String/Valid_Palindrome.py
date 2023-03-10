class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def get_alnum_pointer_of_direction(pointer, direction):
            while 0 <= pointer < len(s) and not s[pointer].isalnum():
                pointer += direction
            return pointer

        while left < right:
            left = get_alnum_pointer_of_direction(left, 1)
            right = get_alnum_pointer_of_direction(right, -1)
            if not (left < right):
                break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
