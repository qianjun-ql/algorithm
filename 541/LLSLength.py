# Program the recurrence for longest stable subsequence
# 0 <= i <= len(a)
# Note that if j == -1, then take aj = None
# else aj = a[j]
def lssLength(a, i, j):
    aj = a[j] if 0 <= j < len(a) else None 
    # Implement the recurrence below. Use recursive calls back to lssLength
    # your code here
    if i == len(a):
        return 0
    
    if aj is not None and abs(a[i] - aj) > 1:
        return lssLength(a, i+1, j)  # Skip current element
    
    return max(
        lssLength(a, i+1, j),           
        1 + lssLength(a, i+1, i)      
    )
