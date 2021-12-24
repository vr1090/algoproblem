def count(n, last='', mapResult={}):
    key = "n"+"-"+str(last)

    if mapResult.get(key) is not None:
        return mapResult[key]

    if n == 0:
        return 1
    else:
        result =0
        vowels = ['a','e','i','o','u']

        for v in vowels:
            if last <= v:
                result += count(n-1, v, mapResult)
                mapResult[key] = result
        return result

    
