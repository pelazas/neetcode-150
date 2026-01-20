class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = deque()

        for char in s:
            if char in close_to_open and stack:
                open_bracket = stack.pop()
                if close_to_open[char] != open_bracket:
                    return False
            else:
                stack.append(char)
        return True if not stack else False