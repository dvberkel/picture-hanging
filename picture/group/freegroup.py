from picture.group.element import Element

class FreeGroup:
    @staticmethod
    def over(*generators):
        return FreeGroup([Element(g) for g in generators])

    def __init__(self, generators):
        self.generators = generators

    def __len__(self):
        return len(self.generators)

    def __getitem__(self, index):
        return self.generators[index]
