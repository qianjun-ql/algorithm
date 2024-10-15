def targetSum(S, i, tgt):
    if tgt < 0:
        return float('inf')
    if i >= len(S):
        return tgt

    take = targetSum(S, i + 1, tgt - S[i])
    skip = targetSum(S, i + 1, tgt)

    return min(take, skip)
