# Parameters:
#  num: str
#  k: int
# return type: str

def smallestAfterRemoving(num, k):
    if num == "":
        return "0"
    elif k == 0:
        return num
    else:
        minimum = int(num)
        for i in range(len(num)):
            newNumber = num[:i] + num[i+1:]
            minimum = min(minimum,0 if len(newNumber) == 0 else int(newNumber))
        
        return smallestAfterRemoving(str(minimum), k-1)

def main():
    number = "825563"
    result = smallestAfterRemoving(number,2)
    assert( result == "2553")
    number = "2"
    result = smallestAfterRemoving(number,1)
    assert("0" == result)


if __name__== "__main__":
    main()

