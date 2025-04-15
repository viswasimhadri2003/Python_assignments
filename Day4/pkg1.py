class Poly():

    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)
    

    def __add__(self, other):
        diff = len(other.coeffs) - len(self.coeffs)
        a_padded = [0] * max(0, diff) + self.coeffs
        b_padded = [0] * max(0, -diff) + other.coeffs

        return Poly(*[x + y for x, y in zip(a_padded, b_padded)])

    def __repr__(self):
        return f"Poly{tuple(self.coeffs)}"