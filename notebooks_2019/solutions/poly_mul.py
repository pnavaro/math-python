def mul(P, Q): 
 
    res = [0] * (len(P) + len(Q) - 1)
    for s_p, s_q in enumerate(P):
        for c_p, c_q in enumerate(Q):
            res[s_p + c_p] += s_q * c_q
            
    return res
