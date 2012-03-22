class FactorsFormatter:
    def __init__(self, factors):
        self.factors = factors

    def __str__(self):
        return "".join([self._format(factor) for factor in self.factors])
    
    def _format(self, factor):
        if (factor[1] == 0):
            return ""
        elif (factor[1] == 1):
            return factor[0]
        else:
            return "{0}^{1}".format(factor[0], factor[1])
