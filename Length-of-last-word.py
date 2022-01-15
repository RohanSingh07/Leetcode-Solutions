# Faster than 85% solution , memory less than 60-70 %
# Logic:- 
# Start from the last until you find a character which is not blank.
# Keep decreasing the index and keep increasing the counter(Length of the last word) until you find a space or the length of the string is reached

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        flag = False
        count = 1
        index = -1
        while length:
            if flag and s[index]!=" ":
                count+=1
            elif flag and s[index]==" ":
                break
            elif flag== False and s[index]!=" ":
                flag = True
            length-=1
            index-=1
        return count
