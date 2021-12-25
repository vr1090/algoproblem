def knapsack(values, weight, maxWeight, i=0):
    if i == len(weight):
        return 0
    
    if weight[i] > maxWeight:
        return knapsack(values, weight, maxWeight, i+1)
    else:
        withTaken = values[i] + knapsack(values, weight, \
            maxWeight- weight[i], i+1)
        withoutTaken = knapsack(values, weight, maxWeight,i+1)
        return max( withTaken, withoutTaken)

def main():
    result =knapsack([12],[28],6)
    print(result)
    assert( result == 0)

if __name__=="__main__":
    main()