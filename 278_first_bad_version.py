# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        
        while left <= right :
            mid = (left + right)//2
            
            if( isBadVersion(mid) and not isBadVersion(mid-1)):
                result = mid
                break
            elif isBadVersion(mid - 1):
                right = mid -1
            else:
                left = mid + 1
        
        
        return result