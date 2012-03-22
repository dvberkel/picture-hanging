class Normalizer:
    @staticmethod
    def of(factors):
        return Normalizer(factors)
    
    def __init__(self, factors):
        self.factors = factors

    def normalize(self):
        index = 0
        while (index < len(self.factors)):
            if (self.factors[index][1] == 0):
                self.factors.pop(index)
                index = 0
                continue
            if (index < len(self.factors) - 1 and self.factors[index][0] == self.factors[index+1][0]):
                self.factors[index] = (self.factors[index][0], self.factors[index][1] + self.factors[index+1][1])
                self.factors.pop(index + 1)
                index = 0
                continue
            index += 1
        return self.factors
