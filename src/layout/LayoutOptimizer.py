import math, random, time
import numpy as np
from .LayoutStrategy import LayoutConvexPoly, LayoutGenetic

def optimize_layout(graph):
    strategy = None
    # if len(graph.regions) == 0:
    #     pass
    if len(graph.regions) == 1 and len(graph.regions[0].ordered_nodes()) == len(graph.graph):
        strategy = LayoutConvexPoly()
    else:
        strategy = LayoutGenetic()
    return strategy.optimize_layout(graph)
