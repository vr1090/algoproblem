class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxSet = 0
        setItem = set()
        
        for j in range(len(s)):
            while s[j] in setItem:
                setItem.remove(s[i])
                i +=1
            
            setItem.add(s[j])
            maxSet = max( maxSet, len(setItem))
            
        
        return maxSet
            

## second version

class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        setChar = set()
        maxChar = 0
        i =0
        j =0
        
        while j < len(str):
            if str[j] in setChar:
                setChar.remove(str[i])
                i+=1
            else:
                setChar.add(str[j])
                maxChar = max( maxChar, j-i + 1)
                j+=1
                
        
        return maxChar
        