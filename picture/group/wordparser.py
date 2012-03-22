class WordParser:
    def __init__(self, word):
        self.word = word

    def factors(self):
        return self._parse(self.word)

    def _parse(self, expression):
        return [(expression[0], int(expression[2]) if len(expression) > 1 else 1)]
