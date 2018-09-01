from solutions.classes.polynomial import Polynomial


class Chebyshev():
    """
    this class generates the sequence of Chebyshev polynomials of the first kind
    """

    def __init__(self, n_max=10):
        self.T_0 = Polynomial([1])
        self.T_1 = Polynomial([0, 1])
        self.n_max = n_max
        self.index = 0
        self.coeffs = self.T_0.coeffs[:]
        self.degree = len(self.coeffs)

    def __iter__(self):
        return self  # Returns itself as an iterator object

    def __next__(self):
        self.index += 1
        if self.index == 1: return Polynomial([1])
        if self.index == self.n_max:
            raise StopIteration()
        self.T_0, self.T_1 = self.T_1, Polynomial([0, 2]) * self.T_1 - self.T_0
        self.coeffs = self.T_0.coeffs[:]
        return self.T_0


if __name__ == "__main__":

    for t in Chebyshev():
        print(t, "; ", t.diff(1))
