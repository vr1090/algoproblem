# Parameters:
#  amount: int
#  coins: Set[int]
# return type: int

def coinChange(amount, coins,memoixe={}):
    # base case dulu
    key = amount

    if memoixe.get(key) is not None:
        return memoixe[key]

    if amount <=0:
        return 0
    else:
        results = float("inf")
        for c in coins:
            if ( amount - c) >=0:
               tryCoin = 1 + coinChange(amount - c, coins)
               results = min( results, tryCoin)

        memoixe[key] = results        
        return results 


logged = True
def logging(*logs):
    if(logged):
        print("setan", logs)

def main():
    memoize = {}
    result = coinChange(64, {1,5}, memoize)
    logging(memoize)
    assert(result == 16)

if __name__=="__main__":
    main()