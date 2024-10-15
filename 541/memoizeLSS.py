def memoizeLSS(a):
    T = {}
    n = len(a)
    
    for j in range(-1, n):
        T[(n, j)] = 0  # No elements left to form a subsequence
    
    for i in range(n-1, -1, -1):
        for j in range(-1, i):
            aj = a[j] if j != -1 else None  # Get the value of aj if j is valid, otherwise None
            

            option_skip = T[(i+1, j)]

            if aj is None or abs(a[i] - aj) <= 1:
                option_take = 1 + T[(i+1, i)]
            else:
                option_take = 0
            
            T[(i, j)] = max(option_skip, option_take)
    
    return T