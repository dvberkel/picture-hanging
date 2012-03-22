class FreeGroup:
    @staticmethod
    def over(*generators):
        return FreeGroup(generators)

    def __init__(self, generators):
        self.generators = generators

    def __len__(self):
        return len(self.generators)
