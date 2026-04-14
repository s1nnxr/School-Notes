
#❖ Úloha: vlastní iterátor
#Vytvořte si vlastní iterátor, který např.
#
#funguje podobně jako range(), nebo
#generuje řadu druhých mocnin, nebo
#generuje prvočísla

class Range():
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current

for i in Range(0, 10, 2):
    print(next(i))
