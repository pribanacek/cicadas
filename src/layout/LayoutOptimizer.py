import math, random, time
import numpy as np

from .Cooling import LinearCooling, ExpCooling

lower = 0
probs = 0
def shouldTransition(energy1, energy2, temp):
    global lower, probs
    if energy1 > energy2:
        lower += 1
        return True
    boltzmann = 1.38e-2
    r = random.random()
    p = np.exp((energy1 - energy2) / (temp * boltzmann))
    if r < p:
        probs += 1
        return True
    return False

def getRadius(temp):
    return temp / 1000

def optimizeLayout(graph):
    dimensions = (4, 4)
    # cooling = LinearCooling(10000, 1, 100)
    cooling = ExpCooling(3000, 1, 0.98)
    graph.randomPlan(dimensions)
    graphs = [graph]
    minGraph = graph
    minEnergy = graph.energy(dimensions)
    while not cooling.done():
        newGraph = graph.randomNeighbour(getRadius(cooling.temp))
        E1 = graph.energy(dimensions)
        E2 = newGraph.energy(dimensions)
        if E2 < minEnergy:
            minGraph = newGraph
            minEnergy = E2
        if shouldTransition(E1, E2, cooling.temp):
            graph = newGraph
        graphs.append(graph)
        cooling.cool()
    minGraph.recentreNodes()
    return (minGraph, graphs)
