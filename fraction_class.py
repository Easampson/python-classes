class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __repr__(self):
        return "%s(%r,%r)" % (self.__class__.__name__,self.num,self.den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self,other):
        othernum = self.num * other.den + self.den * other.num
        otherden = self.den * other.den 
        return Fraction(othernum, otherden)

    def __sub__(self,other):
        othernum = self.num * other.den - self.den
        otherden = self.den * other.den
        return Fraction(othernum,otherden)

    def __mul__(self,other):
        othernum = self.num * other.num
        otherden = self.den * other.den
        return Fraction(othernum, otherden)

    def __div__(self,other):
        othernum = self.num * other.den
        otherden = self.den * other.num
        return Fraction(other,otherden)

    def __gt__(self,other):
        if other.num < self.num and other.den < self.den:
            return True
        else:
            return False

    def __ge__(self,other):
        if other.num <= self.num and other.den <= self.den:
            return True
        else:
            return False

    def __lt__(swlf,other):
        if other.num > self.num and other.den > self.den:
            return True
        else:
            return False

    def __le__(self,other):
        if other.num >= self.num and other.den >= self.den:
            return True
        else:
            return False

    def __ne__(self,other):
        if other.num == self.num and other.den == self.den:
            return False
        else:
            return True 
