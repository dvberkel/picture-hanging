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
                if (expression[1] == '^'):
                    index = 2
                    while (index < len(expression) and expression[index] in string.digits):
                        index += 1
                    number = int(expression[2:index])
                    return [(letter, number)]
            else:
              return [(letter, 1)]
        raise ParseError()

class ParseError:
    pass
        
