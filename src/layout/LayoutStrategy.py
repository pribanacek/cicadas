import math, random, time
import numpy as np
from abc import ABC, abstractmethod
from .Cooling import LinearCooling, ExpCooling

class LayoutStrategy(ABC):
    def __init__(self):
        self.last_progress = 0
    
    def print_progress(self, progress, interval):
        percent = round(100 * progress)
        if self.last_progress // interval != percent // interval:
            self.last_progress = percent
            print('\r optimizing layout... %s%%' % percent, end = '')
            if progress >= 1:
                print('\n')
    
    def initialise_graph_set(self, graph, n):
        graphs = []
        for _ in range(n):
            graph_copy = graph.copy()
            graph_copy.random_plan()
            graphs.append(graph_copy)
        return graphs

    @abstractmethod
    def optimize_layout(self, graph):
        pass


class LayoutSimulatedAnnealing(LayoutStrategy):
    INITIAL_TEMPERATURE = 1000

    def get_radius(self, temp, dimensions):
        factor = max(*dimensions)
        radius = temp / self.INITIAL_TEMPERATURE * factor
        return radius

    def should_transition(self, energy1, energy2, temp):
        if energy1 > energy2:
            return True
        boltzmann = 1.38e-2
        r = random.random()
        p = np.exp((energy1 - energy2) / (temp * boltzmann))
        if r < p:
            return True
        return False
    
    def optimize_layout(self, graph):
        dimensions = graph.dimensions
        cooling = ExpCooling(self.INITIAL_TEMPERATURE, steps = 1000, resets = 0)
        best_graphs = self.initialise_graph_set(graph, 1)
        best_graph = None
        graph_history = [graph]

        while not cooling.done():
            radius = self.get_radius(cooling.get_temp(), dimensions)
            new_graphs = [graph.random_neighbour(radius) for graph in best_graphs]

            for i in range(len(best_graphs)):
                E1 = best_graphs[i].energy()
                E2 = new_graphs[i].energy()
                if best_graph == None or E2 < best_graph.energy():
                    best_graph = new_graphs[i]
                    graph_history.append(best_graph)
                if self.should_transition(E1, E2, cooling.get_temp()):
                    best_graphs[i] = new_graphs[i]
            cooling.cool()
            self.print_progress(cooling.progress(), interval = 2)

        print('FINAL ENERGY', best_graph.energy())
        best_graph.recentre_nodes()
        return (best_graph, graph_history)


class LayoutGenetic(LayoutStrategy):
    INITIAL_TEMPERATURE = 1000
    NUMBER_OF_GRAPHS = 5

    def get_radius(self, temp, dimensions):
        factor = max(*dimensions)
        radius = temp / self.INITIAL_TEMPERATURE * factor
        return radius
    
    def optimize_layout(self, graph):
        dimensions = graph.dimensions
        cooling = ExpCooling(self.INITIAL_TEMPERATURE, steps = 1000, resets = 0)
        best_graphs = self.initialise_graph_set(graph, self.NUMBER_OF_GRAPHS)
        best_graph = None
        graph_history = [graph]
        while not cooling.done():
            radius = self.get_radius(cooling.get_temp(), dimensions)
            new_graphs = [graph.random_neighbour(radius) for graph in best_graphs]
            sorted_graphs = sorted(best_graphs + new_graphs, key = lambda x : x.energy())
            best_graphs = sorted_graphs[:self.NUMBER_OF_GRAPHS]
            if best_graph == None or best_graphs[0].energy() < best_graph.energy():
                best_graph = best_graphs[0]
                graph_history.append(best_graph)

            cooling.cool()
            self.print_progress(cooling.progress(), interval = 2)

        print('FINAL ENERGY', best_graph.energy())
        best_graph.recentre_nodes()
        return (best_graph, graph_history)


class LayoutConvexPoly(LayoutStrategy):
    def optimize_layout(self, graph):
        region = graph.regions[0]
        radius = min(*graph.dimensions) * 0.4
        graph_set = self.initialise_graph_set(graph, len(graph.graph))
        for i in range(len(graph_set)):
            permutation = i
            positions = region.uniform_layout(radius, permutation = permutation)
            for node_id, pos in positions.items():
                graph_set[i].set_node_position(node_id, pos)
        best_graph = min(*graph_set, key = lambda x : x.energy())
        # TODO return worse ones with a certain probability?
        return (best_graph, [best_graph])
