"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        
        # find minimum first
        minimum = 201
        longestPrefix=""
        
        for s in strs:
            minimum = min(minimum, len(s))
            
        
        
        
        for i in range(minimum):
            allIsTrue = True
            
            checkChar = strs[0][i]
            
            for s in strs:
                allIsTrue = allIsTrue and s[i] == checkChar
            
            #print("is all is true", allIsTrue, "::", checkChar)
            if allIsTrue:
                longestPrefix += checkChar
            else:
                break
        
        return longestPrefix
        