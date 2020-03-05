class Path:
    def __init__(self, path):
        if path == None:
            self._pathText = 'id'
            self.edge_ids = ()
        elif type(path) == str:
            self._pathText = path
            self.edge_ids = tuple(reversed(path.split('.')))
        elif type(path) == tuple or type(path) == list:
            self._pathText = '.'.join(reversed(path))
            self.edge_ids = tuple(path)
        else:
            raise Exception('Invalid path type')
    
    def isIdentity(self):
        return self.edge_ids == ()
    
    def __len__(self):
        return len(self.edge_ids)
    
    def __str__(self):
        return self._pathText

    def __eq__(self, other):
        if isinstance(other, Path):
            return self.edge_ids == other.edge_ids
        return False
    
    def __hash__(self):
        return hash(self.edge_ids)
