class Cooling:
    def __init__(self, start, end, decrement):
        self.startTemp = start
        self.endTemp = end
        self.decrement = decrement
        self.temp = start

    def done(self):
        return self.temp < self.endTemp

    def cool(self):
        pass

class LinearCooling(Cooling):
    def cool(self):
        self.temp -= self.decrement

class ExpCooling(Cooling):
    def cool(self):
        self.temp *= self.decrement