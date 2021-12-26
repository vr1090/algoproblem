# Parameters:
#  amount: int
#  coins: Set[int]
# return type: int

def coinChange(amount, coins,memoixe={}):
    # base case dulu
    key = amount
    
    if memoixe.get(key) is not None:
        return memoixe[key]

    logging("need to compute...", amount, memoixe)
    if amount <=0:
        return 0

    if amount < min(coins):
        return float("inf") 
    else:
        results = 2000
        for c in coins:
            if ( amount - c) >=0:
               tryCoin = 1 + coinChange(amount - c, coins, memoixe)
               results = min( results, tryCoin)

        memoixe[key] = results        
        return results 


logged = True
def logging(*logs):
    if(logged):
        print("setan", *logs)

def main():
    memoize = {}
    result = coinChange(15, {3,2,7}, memoize)
    logging("result", result, memoize)
    assert(result == 4)

if __name__=="__main__":
    main()