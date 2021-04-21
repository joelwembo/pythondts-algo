class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(6.0, 4.5) 
print(x.r)   
print(x.i)

print(x.r // x.i)

