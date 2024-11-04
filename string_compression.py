class Solution:
    def compressedString(self, word: str) -> str:
        comp = "" #initialize an empty comp to store the compressed string
        while word: #continue untill word becomes empty
            c = word[0] #store first char in word to c
            length = 0 # to find the lenght of the prefix of repeating characters up to                           a max of 9
            for i in range(min(len(word), 9): # limit checking up to 9 chars
                           if word[i] == c:
                                length += 1
                           else:
                                break

            #append the length followed by the letter stored by c
            comp += str(length) + c 
            #removed processed prefix from word
            word = word[length:]
            return comp
