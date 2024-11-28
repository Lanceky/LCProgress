class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        length1 = len(word1)
        length2 = len(word2)
        min_length = min(length1, length2)  # Find the smaller length to iterate over both strings
        
        # Merge letters in alternating order for the common length
        for i in range(min_length):
            merged_string += word1[i]
            merged_string += word2[i]
        
        # Append remaining characters from the longer string
        if length1 > length2:
            merged_string += word1[min_length:]
        else:
            merged_string += word2[min_length:]
        
        return merged_string


