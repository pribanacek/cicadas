import random

class EdgeStyle:
    def __init__(self, style, overriden_by = None):
        self.alternatives = []
        if type(style) == str:
            self.style = style
        elif type(style) == list:
            self.alternatives = style
            self.random_alternative()
        self.overriden_by = overriden_by
    
    def conflicts(self, styles):
        if self.overriden_by == None:
            return False
        for i in self.overriden_by:
            for j in styles:
                if i in j.style:
                    return True
        return False
    
    def has_alternatives(self):
        return len(self.alternatives) > 1
    
    def random_alternative(self):
        self.style = random.choice(self.alternatives)
        return self.style
    
    def copy(self):
        if self.has_alternatives():
            return EdgeStyle(self.alternatives, overriden_by = self.overriden_by)
        else:
            return EdgeStyle(self.style, overriden_by = self.overriden_by)

bend_shift_loop = ['bend', 'shift', 'loop']

AUTO_BEND = EdgeStyle(['bend left', 'bend right'], overriden_by = bend_shift_loop)
LEFT_BEND = EdgeStyle('bend left', overriden_by = bend_shift_loop)
RIGHT_BEND = EdgeStyle('bend right', overriden_by = bend_shift_loop)

AUTO_LOOP = EdgeStyle(['loop left', 'loop right'], overriden_by = bend_shift_loop)

AUTO_SHIFT = EdgeStyle(['shift left', 'shift right'], overriden_by = bend_shift_loop)
