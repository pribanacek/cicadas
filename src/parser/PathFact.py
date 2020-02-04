class PathFact:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def paths(self):
        return (self._x, self._y)
        
    def __str__(self):
        return 'PathFact(' + str(self._x) + ', ' + str(self._y) + ')'
    
    def __eq__(self, other):
        if isinstance(other, PathFact):
            if self._x == other._x and self._y == other._y:
                return True
            if self._x == other._y and self._y == other._x:
                return True
        return False
    
    def __hash__(self):
        pairA = (self._x, self._y)
        pairB = (self._y, self._x)
        return min(hash(pairA), hash(pairB))
