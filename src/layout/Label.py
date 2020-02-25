import numpy as np

LEFT = 'left'
RIGHT = 'right'

class Label:
    def __init__(self, text, latex = False):
        self.label_size = np.array((0, 0))
        self.position = LEFT
        if text == None or latex and text.startswith('_'):
            self.text = ''
        elif latex:
            self.text = '$' + text + '$'
        else:
            self.text = text

    def __str__(self):
        return str(self.text)
