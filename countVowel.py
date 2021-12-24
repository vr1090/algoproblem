def count(n):
    return len( recFind("",["a","i","u","e","o"]))

def recFind(currentResult, possible):
    if len(currentResult) == 2:
        return [currentResult]
    
    results = []
    for x in possible:
        tryChar = possible.pop(0)
        newResult = recFind(currentResult+tryChar, possible)
        results.extend(newResult)
    
    return results

    
