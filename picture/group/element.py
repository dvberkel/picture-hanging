class Element:
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return self.word == other.word

    def __str__(self):
        return self.word
    
    def __repr__(self):
        return "Element(\"{0}\")".format(self.word)
