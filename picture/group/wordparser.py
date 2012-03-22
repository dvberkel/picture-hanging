class WordParser:
    def __init__(self, word):
        self.word = word

    def factors(self):
        return [(self.word, 1)]
