def getBestTargetSum(S, tgt):
    k = len(S)
    assert tgt >= 0
    

    T = {}
    Choices = {} 
    

    for j in range(tgt + 1):
        T[(k, j)] = j  
        Choices[(k, j)] = False
    

    def lookupMemoTable(i, j):
        if j < 0:
            return float('inf')
        if (i, j) not in T:
            take = lookupMemoTable(i + 1, j - S[i])
            skip = lookupMemoTable(i + 1, j)
            
            if take <= skip:
                T[(i, j)] = take
                Choices[(i, j)] = True
            else:
                T[(i, j)] = skip
                Choices[(i, j)] = False
        
        return T[(i, j)]
    

    lookupMemoTable(0, tgt)
    

    res = []
    i, j = 0, tgt
    while i < k and j >= 0:
        if Choices[(i, j)]:
            res.append(S[i])
            j -= S[i]
        i += 1
    
    return res