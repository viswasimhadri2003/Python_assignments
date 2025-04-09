class Poly:
    def __init__(self, *coefficients):
        """Initialize the polynomial with coefficients."""
        self.coefficients = list(coefficients)

    def __str__(self):
        """Return a string representation of the polynomial."""
        return "Poly(" + ", ".join(map(str, self.coefficients)) + ")"

    def __add__(self, other):
        """Add two polynomials."""
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [0] * max_len

        for i in range(1,len(self.coefficients)+1):
            new_coefficients[-i] += self.coefficients[-i] #adding coefficients to last of the new_polynomial

        for i in range(1,len(other.coefficients)+1):
            new_coefficients[-i] += other.coefficients[-i]

        return Poly(*new_coefficients)

if __name__ == "__main__":
        a = Poly(1, 2, 3)  # Represents polynomial 1x² + 2x + 3
        b = Poly(1, 0, 1, 1, 2, 3)  # Represents polynomial 1x⁵ + 0x⁴ + 1x³ + 1x² + 2x + 3
        c = Poly.__add__(a,b)  # Add the two polynomials
        print(c)  # Output: Poly(1, 0, 1, 2, 4, 6)

