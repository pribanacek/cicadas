import math, random, time
import numpy as np

from .Cooling import LinearCooling, ExpCooling

INITIAL_TEMPERATURE = 1000

lower = 0
probs = 0
def should_transition(energy1, energy2, temp):
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

def get_radius(temp, dimensions):
    factor = max(*dimensions)
    radius = temp / INITIAL_TEMPERATURE * factor
    return radius

NUMBER_OF_GRAPHS = 5

def initialise_graph_set(graph):
    graphs = []
    for _ in range(NUMBER_OF_GRAPHS):
        graph_copy = graph.copy()
        graph_copy.random_plan()
        graphs.append(graph_copy)
    return graphs

def optimize_layout(graph):
    graph.dimensions = (16, 16) # TODO remove

    dimensions = graph.dimensions
    # cooling = LinearCooling(INITIAL_TEMPERATURE, 1, 100)
    cooling = ExpCooling(INITIAL_TEMPERATURE, 1, 0.98)
    best_graphs = initialise_graph_set(graph)
    best_graph = None
    graph_history = [graph]
    while not cooling.done():
        radius = get_radius(cooling.temp, dimensions)
        new_graphs = [graph.random_neighbour(radius) for graph in best_graphs]
        # simulated annealing
        # for i in range(len(best_graphs)):
        #     E1 = best_graphs[i].energy(dimensions)
        #     E2 = new_graphs[i].energy(dimensions)
        #     if best_graph == None or E2 < best_graph.energy(dimensions):
        #         best_graph = new_graphs[i]
        #         graph_history.append(best_graph)
        #     if should_transition(E1, E2, cooling.temp):
        #         best_graphs[i] = new_graphs[i]

        # genetic algorithm
        sorted_graphs = sorted(best_graphs + new_graphs, key = lambda x : x.energy())
        best_graphs = sorted_graphs[:NUMBER_OF_GRAPHS]
        if best_graph == None or best_graphs[0].energy() < best_graph.energy():
            best_graph = best_graphs[0]
        cooling.cool()
    print('FINAL ENERGY', best_graph.energy())
    best_graph.recentre_nodes()
    return (best_graph, graph_history)
