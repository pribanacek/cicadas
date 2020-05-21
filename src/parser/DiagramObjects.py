import numpy as np

from src.layout.Label import Label

class Object:
    def __init__(self, node_name, label = None):
        self.node_name = node_name
        self.label = Label(label) if label != None else Label(node_name, latex = True)

    def set_label(self, label_text):
        self.label = Label(label_text)
    
    def set_label_size(self, size):
        self.label.label_size = np.array(size)

class Morphism:
    def __init__(self, edge_id, start, end, label = None, styles = None):
        self.edgeId = edge_id
        self.start = start
        self.end = end
        self.styles = [] if styles == None else styles
        self.auto_styles = []
        if label != None:
            self.set_label(label)
        else:
            self.label = Label(edge_id, latex = True, edge_label = True)
    
    def add_auto_style(self, style):
        if not style.conflicts(self.styles):
            self.auto_styles.append(style)
    
    def has_alternatives(self):
        return any(s.has_alternatives() for s in self.auto_styles)
        
    def get_styles(self):
        styles = self.styles + self.auto_styles
        return list(map(lambda x : x.style, styles))

    def set_label(self, label_text):
        self.label = Label(label_text, edge_label = True)
    
    def set_label_size(self, size):
        self.label.label_size = np.array(size)
