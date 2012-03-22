import string

class WordParser:
    def __init__(self, word):
        self.word = word

    def factors(self):
        return self._parse(self.word)

    def _parse(self, expression):
        if (expression[0] in string.letters):
            letter = expression[0]
            if (len(expression) > 1):
                return [(letter, int(expression[2]))]
            else:
              return [(letter, 1)]
        raise ParseError()

class ParseError:
    pass
        
