class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(!r'

p1 = Polynomial(1,3,4)
p2 = Polynomial(4,6,8)

print(p1)