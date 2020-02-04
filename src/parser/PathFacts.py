from src.parser.PathFact import PathFact as PathFact

class PathFacts:
    def __init__(self):
        self.pathFacts = set()
        self.inferredFacts = set()
        self.inferred = True

    def addFact(self, pathA, pathB):
        self.inferred = False
        pair = PathFact(pathA, pathB)
        self.pathFacts.add(pair)
    
    def getFacts(self):
        return self.pathFacts
    
    def getAllFacts(self):
        if not self.inferred:
            self.inferPathFacts()
        return self.pathFacts | self.inferredFacts
    
    # def replaceOccurrences(self, factToReplace, facts):
        
    def inferPathFacts(self):
        self.inferred = True
        self.inferredPairs = set()
        factDict = {}
        maxLen = 0
        for pair in self.pathFacts:
            (pathA, pathB) = pair.paths()
            factDict[pathA] = pathB
            factDict[pathB] = pathA
            maxLen = max(maxLen, len(pathA), len(pathB))
        # replaceTuple = lambda x, i, length, y: tuple(list(x)[:i] + list(y) + list(x)[i+length:])
        # i = 1
        # while i <= maxLen:
        #     newFacts = {}
        #     for key, value in factDict.items():
        #         if len(key) < i:
        #             continue
        #         prefix = key[0:i]
        #         suffix = key[i:]
        #         for k, v in factDict.items():
        #             if key == k or key == v:
        #                 continue
        #             if v[len(v) - i:] == prefix:
        #                 newK = concatTuple(k, suffix)
        #                 newV = replaceTuple(v, len(v) - i, i, value)
        #                 (trimmedK, trimmedV) = trimPaths(newK, newV)
        #                 if validPathPair(trimmedK, trimmedV):
        #                     newFacts[trimmedK] = trimmedV
        #                     newFacts[trimmedV] = trimmedK
        #                     maxLen = max(maxLen, len(trimmedK), len(trimmedV))
        #             elif v[:i] == suffix:
        #                 newK = concatTuple(prefix, k)
        #                 newV = replaceTuple(v, 0, i, value)
        #                 (trimmedK, trimmedV) = trimPaths(newK, newV)
        #                 if validPathPair(trimmedK, trimmedV):
        #                     newFacts[trimmedK] = trimmedV
        #                     newFacts[trimmedV] = trimmedK
        #                     maxLen = max(maxLen, len(trimmedK), len(trimmedV))
        #     factDict = {**newFacts, **factDict} # merge the dictionaries
        #     i += 1
        
        # for k, v in factDict.items():
        #     # (pathA, pathB) = trimPaths(k, v)
        #     pathA, pathB = k, v
        #     if len(pathA) > 0 and len(pathB) > 0:
        #         pair = PathFact(pathA, pathB)
        #         if pair not in self.pathFacts and pair not in self.inferredFacts:
        #             self.inferredPairs.add(pair)
