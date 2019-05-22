def findPoisonedDuration(timeSeries, duration):
    if not timeSeries: return 0
    n = len(timeSeries)
    time = duration
    if n == 1: return time
    for i in range(1, n):
        time += min(duration, timeSeries[i] - timeSeries[i - 1])
    return time
timeSeries = [1,2,5,7,10,14,15,17]
duration = 2
print(findPoisonedDuration(timeSeries,duration))