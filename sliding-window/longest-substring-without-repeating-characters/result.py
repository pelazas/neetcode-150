class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        result = 0
        for i in range(len(s)):
            char = s[i]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            
            seen[char] = i
            result = max(result, i-l+1)
        return result
        