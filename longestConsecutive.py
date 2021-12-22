# Parameters:
#  arr: List[int]
# return type: int

def longestConsecutiveSequence(arr):
    if len(arr) < 2:
        return len(arr)

    sorted(arr)
    longest = 1
    maxLongest = 0
    for i in range(1,len(arr)):
        if( arr[i-1]== arr[i]-1):
            longest += 1
        else:
            longest = 1
        
        maxLongest = max( maxLongest, longest)
    
    return maxLongest

def longestConsecutiveSequence2(arr):
    if len(arr) < 2:
        return len(arr)
    
    maxLength = 1
    length = 1
    arr.sort()

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]+1:
            length += 1
        elif arr[i] == arr[i-1]:
            pass
        else:
            length=1
        maxLength= max(maxLength, length)
    
    return maxLength



def main():
    arr = [5,1,2,3,7]
    result = longestConsecutiveSequence2(arr)
    print(result)
    assert( 3 == result)
    result = longestConsecutiveSequence([0,1,2,4,6,7,8,9,13,14])
    assert(4 == result)

if __name__ == "__main__":
    main()