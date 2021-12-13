# Parameters:
#  arr: List[int]
# return type: List[int]

def productExceptSelf(arr):
    lengthN = len(arr)
    leftSum = [0] * lengthN
    rightSum = [0] * lengthN

    # right sum first
    rightSum[lengthN-1] = 1
    for i in range(lengthN-2,-1,-1):
        rightSum[i] = rightSum[i+1] * arr[i+1]

    leftSum[0] =1 

    for i in range(1, lengthN):
        leftSum[i] = leftSum[i-1] * arr[i-1]
    
    total = [ leftSum[i] * rightSum[i] for i in range(0,lengthN)]

    return total


def main():
    print(productExceptSelf([2,5,3,4]))

if __name__ == "__main__":
    main()