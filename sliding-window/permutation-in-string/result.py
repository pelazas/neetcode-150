class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_s1 = [0] * 26
        for c in s1:
            char_index = ord(c)-ord('a')
            frequency_s1[char_index] +=1

        frequency_s2 = [0] * 26
        for c in s2[:len(s1)]:
            char_index = ord(c)-ord('a')
            frequency_s2[char_index] +=1
        
        if frequency_s2 == frequency_s1:
            return True

        for r in range(len(s1), len(s2)):
            l = r-len(s1)
            old_char = s2[l]
            new_char = s2[r]
            
            frequency_s2[ord(old_char)-ord('a')] -=1
            frequency_s2[ord(new_char)-ord('a')] +=1

            if frequency_s2 == frequency_s1:
                return True

        return False


        