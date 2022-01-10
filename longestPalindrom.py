class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        maxLength = 1
        for i in range(len(s)):
            l,r = i,i
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                maxLength = max( maxLength, r-l + 1)
            
                if( len(palindrome) < maxLength):
                    palindrome = str(s[l:r+1])
                
                l = l -1
                r = r+1
            
            
            l,r = i,i+1
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                maxLength = max( maxLength, r-l + 1)
            
                if( len(palindrome) < maxLength):
                    palindrome = str(s[l:r+1])
                
                l = l -1
                r = r+1
            
        return palindrome
        