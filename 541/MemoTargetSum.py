def memoTargetSum(S, tgt):
    k = len(S)
    assert tgt >= 0
    

    T = {}
    
    
    for j in range(tgt + 1):
        T[(k, j)] = j  

    for i in range(k + 1):
        T[(i, 0)] = 0 
    

    def lookupMemoTable(i, j):
        if j < 0:
            return float('inf')
        if (i, j) not in T:
            if i == k: 
                T[(i, j)] = j
            else:

                take = lookupMemoTable(i + 1, j - S[i]) 
                skip = lookupMemoTable(i + 1, j)  
                T[(i, j)] = min(take, skip) 
        return T[(i, j)]
    

    for j in range(tgt + 1):
        lookupMemoTable(0, j)
    
    return T