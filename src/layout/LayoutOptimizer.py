import math, random, time
import numpy as np
from .LayoutStrategy import LayoutConvexPoly, LayoutSimulatedAnnealing

# delegates the given graph to the appropriate layout strategy
def optimize_layout(graph, output_number, iterations):
    strategy = None
    if len(graph.regions) == 1 and len(graph.regions[0].ordered_nodes()) == len(graph.graph):
        strategy = LayoutConvexPoly()
    else:
        strategy = LayoutSimulatedAnnealing()
    return strategy.optimize_layout(graph, output_number, iterations)
