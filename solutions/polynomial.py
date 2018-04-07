from IPython.display import Math, display
class Polynomial:
    """ Polynomial """
    def __init__( self, coefficients):
        self.coeffs = coefficients
        self.degree = len(coefficients)

    def diff(self, n):
        """ Return the nth derivative """
        coeffs = self.coeffs[:]
        for k in range(n):
            coeffs = [i * coeffs[i] for i in range(1,len(coeffs))]
        return Polynomial(coeffs)

    def __repr__(self):
        output = ""
        for i, c  in enumerate(self.coeffs):
            output += "{0:+d}x^{1}".format(c,i)
        return output

    def pprint(self):
        display(Math(self.__repr__()))

    def __eq__(self, Q): # override '=='
        return self.coeffs == Q.coeffs

    def __add__( self, Q):  #  ( P + Q )
        if self.degree < Q.degree:
            coeffs = self.coeffs + [0]*(Q.degree - self.degree)
            return Polynomial([c+q for c,q in zip(Q.coeffs,coeffs)])
        else:
            coeffs = Q.coeffs + [0]*(self.degree - Q.degree)
            return Polynomial([c+q for c,q in zip(self.coeffs,coeffs)])

    def __neg__(self):
        return Polynomial([-c for c in self.coeffs])

    def __sub__(self, Q):
        return self.__add__(-Q)

    def __mul__(self, Q): # (P * Q) or (alpha * P)

        if isinstance(Q, Polynomial):
            _s = self.coeffs
            _q = Q.coeffs
            res = [0]*(len(_s)+len(_q)-1)
            for s_p,s_c in enumerate(_s):
                for q_p, q_c in enumerate(_q):
                    res[s_p+q_p] += s_c*q_c
            return Polynomial(res)
        else:
            return Polynomial([c*Q for c in self.coeffs])

if __name__ == "__main__":
    P = Polynomial([-3,-1,1,-1,4])
    Q = P.diff(2)
    S = -P
    print(P)
    print(Q)
    print(S)
    print(P+Q)
    print(Q+P)
