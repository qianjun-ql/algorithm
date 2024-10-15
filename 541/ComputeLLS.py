def computeLSS(a):
    T = memoizeLSS(a) 
    subsequence = []
    i, j = 0, -1
    
    while i < len(a):

        aj = a[j] if j != -1 else None
        option_skip = T[(i+1, j)] 

        if aj is None or abs(a[i] - aj) <= 1:
            option_take = 1 + T[(i+1, i)]
        else:
            option_take = 0

        if option_take > option_skip:
            subsequence.append(a[i])
            j = i 
        
        i += 1
    
    return subsequence