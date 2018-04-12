def diff(P, n):
    """ Return the nth derivative of polynom P """
    if n == 0:
        return P
    else:
        return diff([i * P[i] for i in range(1,len(P))], n-1)

print(diff([3,2,1,5,7],2))
print(diff([-6,5,-3,-4,3,-4],3))
