class Calc:
    MODE_NORMAL = 0
    MODE_VERBOSE = 1
    def __init__(self, mode=MODE_NORMAL):
        self.mode = mode

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

