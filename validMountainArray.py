class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = len(arr) -1
        
        while( i < len(arr)-1 ):
            if( arr[i] < arr[i+1]):
                i+= 1
            else:
                break
        
        while( j > 0 ):
            if( arr[j] < arr[j-1]):
                j -= 1
            else:
                break
        
        return i == j and i != 0 and  j!= len(arr)-1
        