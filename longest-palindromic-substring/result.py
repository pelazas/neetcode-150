class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        starting_index = 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(i,i,s)
            len2 = self.expandFromCenter(i,i+1,s)
            current_len = max(len1,len2)

            #update if found the longest
            if current_len > max_length:
                max_length = current_len
                starting_index = i - ((current_len-1) // 2)
        
        return s[starting_index: starting_index+max_length]

    def expandFromCenter(self, left, right,s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1