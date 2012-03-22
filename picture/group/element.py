from picture.group.wordparser import WordParser
from picture.group.formatter import FactorsFormatter
from picture.group.normalizer import Normalizer

class Element:
    @staticmethod
    def word(word):
        return Element(WordParser(word).factors())
    
    def __init__(self, factors):
        self.factors = Normalizer.of(factors).normalize()

    def inverse(self):
        inverseFactors = [(f[0], -f[1]) for f in self.factors]
        inverseFactors.reverse()
        return Element(inverseFactors)

    def commutate(self, other):
        return self * other * self.inverse() * other.inverse()

    def remove(self, letter):
        return Element([f for f in self.factors if f[0] != letter])

    def __mul__(self, other):
        return Element(self.factors + other.factors)

    def __eq__(self, other):
        return self.factors == other.factors

    def __str__(self):
        return str(FactorsFormatter(self.factors))
    
    def __repr__(self):
        return "Element(\"{0}\")".format(self)
