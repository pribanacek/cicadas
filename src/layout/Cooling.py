from abc import ABC, abstractmethod
import math

# Abstract class for a simulated annealing cooling schedule
class Cooling(ABC):
    def __init__(self, start, end = 0.1, steps = 100, resets = 0):
        self.start_temp = start
        self.end_temp = end
        self.total_steps = steps
        self.resets = resets
        self.step = 0
        self.runs = 0

    def done(self):
        return self.step >= self.total_steps

    def cool(self):
        self.step += 1
        if self.done() and self.runs < self.resets:
            self.runs += 1
            self.step = 0
    
    def progress(self):
        steps_taken = self.runs * self.total_steps + self.step
        total_steps = self.total_steps * (self.resets + 1)
        return steps_taken / total_steps

    @abstractmethod
    def get_temp(self):
        pass

class LinearCooling(Cooling):
    def get_temp(self):
        x = self.step / self.total_steps
        t = (1 - x) * self.start_temp + x * self.end_temp
        return t

class ExpCooling(Cooling):
    def get_temp(self):
        x = self.step / self.total_steps
        k = math.log(self.start_temp / self.end_temp)
        t = self.start_temp * math.exp(-k * x)
        return t

class SigmoidCooling(Cooling):
    def get_temp(self):
        x = self.step / self.total_steps
        k = 10
        t = self.start_temp * (1 + math.exp(k * x - k / 2))
        return t
