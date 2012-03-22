class WordParser:
    def __init__(self, word):
        self.word = word

    def factors(self):
        return [(self.word[0], int(self.word[2]) if len(self.word) > 1 else 1)]
