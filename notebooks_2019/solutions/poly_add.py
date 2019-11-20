from itertools import zip_longest

def add(P, Q):
        
    return [p + q for p, q in zip_longest(P, Q, fillvalue=0)]

P = [ 1, 5, 6, 8]
Q = [0, 1, 0]

add(P, Q)
     
