# Parameters:
#  intervals: List[List[int]]
#  newInterval: List[int]
# return type: List[List[int]]

def insertInterval(intervals, newInterval):
    newInterval = []
    foundMerge = False

    for i in range(len(intervals)):
        if len(newInterval) > 1 and intervals[i][1] >= newInterval[0]:
            foundMerge = True
            intervals[i][0] = min( intervals[i][0], newInterval[0])
            intervals[i][1] = max( intervals[i][1], newInterval[1])
    
    if not foundMerge:
        intervals.append(newInterval)
    
    intervals.sort( key= lambda x: x[0])

    return intervals