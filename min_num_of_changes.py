class Solution:
    def minChanges(self, s: str) -> int:
        change_made = 0
        s_list = list(s)
        
        # Iterate over the string by pairs of two (0, 2, 4, ...)
        for i in range(0, len(s_list) - 1, 2):
            # Check if the current character and the next are different
            if s_list[i] != s_list[i + 1]:
                # Change the next character to match the current 1
                s_list[i + 1] = s_list[i]
                change_made += 1
                
        return change_made
