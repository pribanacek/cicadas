import numpy as np

LEFT = 'left'
RIGHT = 'right'

# Wrapper for node and edge labels
class Label:
    def __init__(self, text, latex = False, edge_label = False, font_size = None):
        self.label_size = np.array((0, 0), dtype = float)
        self.position = LEFT
        self.edge_label = edge_label
        self.font_size = font_size
        if text == None or latex and text.startswith('_'):
            self.text = ''
        elif latex:
            self.text = '$' + text + '$'
        else:
            self.text = text
    
    def empty(self):
        return self.text == ''

    def __str__(self):
        return str(self.text)
    
    def set_label_width(self, width):
        self.label_size[0] = width

    def set_label_height(self, height):
        self.label_size[1] = height
