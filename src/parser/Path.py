class Path:
    def __init__(self, path):
        if path == None:
            self._pathText = 'id'
            self.edgeIds = ()
        elif type(path) == str:
            self._pathText = path
            self.edgeIds = tuple(reversed(path.split('.')))
        elif type(path) == tuple or type(path) == list:
            self._pathText = '.'.join(reversed(path))
            self.edgeIds = tuple(path)
        else:
            raise Exception('Invalid path type')
    
    def isIdentity(self):
        return self.edgeIds == ()
    
    def __len__(self):
        return len(self.edgeIds)
    
    def __str__(self):
        return self._pathText

    def __eq__(self, other):
        if isinstance(other, Path):
            return self.edgeIds == other.edgeIds
        return False
    
    def __hash__(self):
        return hash(self.edgeIds)
