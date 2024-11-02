class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split sentence into words
        words = sentence.split()
        
        # If there's only one word, check if first and last characters match
        if len(words) == 1:
            return words[0][0] == words[0][-1]
        
        # Check each consecutive pair of words
        for i in range(len(words)):
            current_word = words[i]
            next_word = words[(i + 1) % len(words)]  # Use modulo to wrap around to first word
            
            # Get last char of current word and first char of next word
            last_char = current_word[-1]
            first_char = next_word[0]
            
            # If they don't match, sentence is not circular
            if last_char != first_char:
                return False
        
        return True
