from abc import ABC, abstractmethod

class Cooling(ABC):
    def __init__(self, start, end, factor = None, steps = 100, resets = 0):
        self.start_temp = start
        self.end_temp = end
        self.temp = start
        self.runs = 0
        self.resets = resets
        if factor != None:
            self.factor = factor
        else:
            self.factor = self._find_factor(steps)

    def done(self):
        return self.temp < self.end_temp

    def cool(self):
        self._decrease_temp()
        if self.done() and self.runs < self.resets:
            self.runs += 1
            self.temp = self.start_temp

    @abstractmethod
    def _decrease_temp(self):
        pass
    
    @abstractmethod
    def _find_factor(self, steps):
        pass

class LinearCooling(Cooling):
    def _find_factor(self, steps):
        return (self.start_temp - self.end_temp) / steps

    def _decrease_temp(self):
        self.temp -= self.factor

class ExpCooling(Cooling):
    def _find_factor(self, steps):
        return (self.end_temp / self.start_temp) ** (1 / steps)

    def _decrease_temp(self):
        self.temp *= self.factor
