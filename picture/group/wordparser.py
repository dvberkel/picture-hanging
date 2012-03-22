import string

class WordParser:
    def __init__(self, word):
        self.word = word

    def factors(self):
        return self._parse(self.word)

    def _parse(self, expression):
        if (len(expression) == 0):
            return []
        if (expression[0] in string.letters):
            letter = expression[0]
            if (len(expression) > 1):
                if (len(expression) > 2 and expression[1] == '^'):
                    start = 2
                    index = (start + 1) if expression[start] == '-' else start
                    while (index < len(expression) and expression[index] in string.digits):
                        index += 1
                    try:
                        number = int(expression[start:index])
                        return [(letter, number)]
                    except ValueError:
                        pass
            else:
              return [(letter, 1)]
        raise ParseError()

class ParseError:
    pass
        
