class SoBigException(Exception):
    pass


class Calc:
    MODE_NORMAL = 0
    MODE_VERBOSE = 1
    WORD_NUM_MAP = {
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
    def __init__(self, mode=MODE_NORMAL):
        self.mode = mode

    def add(self, a, b):
        if self.mode == Calc.MODE_NORMAL:
            return a + b
        elif self.mode == Calc.MODE_VERBOSE:
            a = Calc.WORD_NUM_MAP[a]
            b = Calc.WORD_NUM_MAP[b]
            rev_map = dict(map(lambda p: (p[1], p[0]), Calc.WORD_NUM_MAP.items()))
            res = a + b
            if res > 10:
                raise SoBigException
            return rev_map[res]

    def sub(self, a, b):
        return a - b

