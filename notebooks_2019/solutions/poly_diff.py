# with recursion
def diff(P, n):
    for d in range(n):
        Q = P.copy()
        if (len(Q) > 1):
            P = [ (e+1)*c for e,c in enumerate(Q[1:])]
        else:
            return [0]
    return P

# with recursion
def diff(p, n):
    """ Return the nth derivative of polynom P """
    if n == 0:
        return p
    else:
        return diff([i * p[i] for i in range(1, len(p))], n - 1)


print(diff([3, 2, 1, 5, 7], 2))
print(diff([-6, 5, -3, -4, 3, -4], 3))

