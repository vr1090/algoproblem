# Parameters:
#  n: int
#  possibleSteps: Set[int]
# return type: int

def waysToClimb(n, possibleSteps):
    possible = []
    def ways(n, count):
        if count >= n:
            possible.append(count)
        else:
            for x in possibleSteps:
                ways(n, count + x)
    
    ways(n,0)

    count = 0
    for c in possible:
        if c == n:
            count += 1
    
    return count

def waysToClimb2(n, possibleStep):
    dpTable = [0] * (n+1)
    dpTable[0] = 1

    for index in range(1, n+1):
        solution = 0
        for step in possibleStep:
            if( index - step) >=0:
                solution += dpTable[index-step]
        dpTable[index] = solution
    return dpTable[n]

def main():
    result = waysToClimb(5,{1,3,4})
    assert( 6 == result)
    result = waysToClimb2(5, {1,3,4})
    print(result)
    assert( 6 == result)

if __name__ == "__main__":
    main()