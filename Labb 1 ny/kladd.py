class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num, "/",self.den)
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)
    def gcd(m,n):
        while m%n !=0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print(f3)