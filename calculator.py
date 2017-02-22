class SoBigException(Exception):
    pass

class SoSmallException(Exception):
    pass

class Calc:
    MODE_NORMAL = 0
    MODE_VERBOSE = 1
    WORD_TO_NUM = {
            'ZERO': 0,
            'ONE': 1,
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'SEVEN': 7,
            'EIGHT': 8,
            'NINE': 9,
            'TEN': 10,
    }
    NUM_TO_WORD = dict(map(lambda p: (p[1], p[0]), WORD_TO_NUM.items()))

    def __init__(self, mode=MODE_NORMAL):
        self.mode = mode

    def add(self, a, b):
        a, b = self.normalize(a), self.normalize(b)
        res = a + b
        if res > 10:
            raise SoBigException
        return self.normalize_res(res)

    def sub(self, a, b):
        a, b = self.normalize(a), self.normalize(b)
        res = a - b
        if res < 0:
            raise SoSmallException
        return self.normalize_res(res)

    def normalize_res(self, val):
        if self.mode == Calc.MODE_VERBOSE:
            return Calc.NUM_TO_WORD[val]
        return val

    def normalize(self, val):
        if self.mode == Calc.MODE_VERBOSE:
            return Calc.WORD_TO_NUM[val]
        return val
