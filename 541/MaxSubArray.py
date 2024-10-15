def maxSubArray(a):
    n = len(a)
    if n == 1:
        return 0
    # your code here
    minSoFar = float('inf')
    maxDiff = float('-inf')
    
    for i in range(n):
        maxDiff = max(maxDiff, a[i] - minSoFar)
        minSoFar = min(minSoFar, a[i])
        
    return maxDiff