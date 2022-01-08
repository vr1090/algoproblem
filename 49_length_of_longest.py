class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i_pointer = 0
        j_pointer = 0
        maxLength = 0
        charSet = set()

        while j_pointer < len(s):
            if s[j_pointer] in charSet:
                charSet.remove(s[i_pointer])
                i_pointer +=1
            else:
                charSet.add(s[j_pointer])
                j_pointer+= 1
                maxLength = max(maxLength, len(charSet))
            
            print("the set", charSet)
        
        return maxLength

if __name__ =="__main__":
    solution = Solution()
    result = solution.lengthOfLongestSubstring("abccd")
    print(result)
    assert(3 == result)

        