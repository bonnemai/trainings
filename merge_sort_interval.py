
def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    results=[]
    if len(intervals)==0:
        return []
    current_interval=intervals[0]
    for i in range(1,len(intervals)): 
        if current_interval[1]<intervals[i][0]: 
            results.append(current_interval)
            current_interval = intervals[i]
        else:
            current_interval=[current_interval[0], intervals[i][1]]
    return results