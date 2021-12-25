def insertInterval(interval, newInterval):
    i =0
    result =[]

    # before

    # just for the before
    while i < len(interval) and interval[i][1] < newInterval[0]:
        result.append(interval[i])
        i +=1
    
    #expands the newInterval
    while i < len(interval) and interval[i][0] <= newInterval[1]:
        newInterval[0] = min( interval[i][0], newInterval[0])
        newInterval[1] = max( interval[i][1], newInterval[1])
        i+=1
    
    # add to the result
    result.append(newInterval)

    #finish all
    while i < len(interval):
        result.append( interval[i])
        i+=1

    return result

def main():
