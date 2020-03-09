import math, random, time
import numpy as np
from abc import ABC, abstractmethod
from src.util.Logging import warn
from .Cooling import LinearCooling, ExpCooling, SigmoidCooling

GRAPH_ENERGY = lambda x : x.energy()

class LayoutStrategy(ABC):
    def __init__(self):
        self.last_progress = 0
    
    def print_progress(self, progress, interval):
        percent = round(100 * progress)
        if self.last_progress // interval != percent // interval:
            self.last_progress = percent
            print('\rGenerating layout... %s%%' % percent, end = '')
            if percent >= 100:
                print()
    
    def initialise_graph_set(self, graph, n):
        graphs = []
        for _ in range(n):
            graph_copy = graph.copy()
            graph_copy.random_plan()
            graphs.append(graph_copy)
        return graphs

    @abstractmethod
    def optimize_layout(self, graph, output_number, quality):
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
        with np.errstate(invalid = 'ignore'):
            p = np.exp((energy1 - energy2) / (temp * boltzmann))
            if r < p:
                return True
        return False
    
    def optimize_layout(self, graph, output_number, quality):
        # x = quality / 4
        # steps = 250 * (x % 1) + 250
        # resets = math.floor(x)
        # print(steps, resets)
        dimensions = graph.dimensions
        cooling = ExpCooling(self.INITIAL_TEMPERATURE, steps = 350, resets = 1)
        n = output_number + 2
        best_graphs = self.initialise_graph_set(graph, n)
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
                    graph_history.append(graph)
                if self.should_transition(E1, E2, cooling.get_temp()):
                    best_graphs[i] = new_graphs[i]
                    if i == 0:
                        graph_history.append(graph)
            cooling.cool()
            self.print_progress(cooling.progress(), interval = 2)
        
        result_graphs = list(sorted(best_graphs, key = GRAPH_ENERGY))[0:output_number]
        for g in result_graphs:
            g.recentre_nodes()

        return (result_graphs, graph_history)


class LayoutGenetic(LayoutStrategy):
    INITIAL_TEMPERATURE = 1000

    def get_radius(self, temp, dimensions):
        factor = max(*dimensions)
        radius = temp / self.INITIAL_TEMPERATURE * factor
        return radius
    
    def optimize_layout(self, graph, output_number, quality):
        dimensions = graph.dimensions
        cooling = ExpCooling(self.INITIAL_TEMPERATURE, steps = 1000, resets = 0)
        n = max(output_number, 4) + 1
        best_graphs = self.initialise_graph_set(graph, n)
        best_graph = None
        graph_history = [graph]
        while not cooling.done():
            radius = self.get_radius(cooling.get_temp(), dimensions)
            new_graphs = [graph.random_neighbour(radius) for graph in best_graphs]
            sorted_graphs = sorted(best_graphs + new_graphs, key = GRAPH_ENERGY)
            best_graphs = sorted_graphs[:n]
            if best_graph == None or best_graphs[0].energy() < best_graph.energy():
                best_graph = best_graphs[0]
                graph_history.append(best_graph)

            cooling.cool()
            self.print_progress(cooling.progress(), interval = 2)

        result_graphs = best_graphs[0:output_number]
        for g in result_graphs:
            g.recentre_nodes()

        return (result_graphs, graph_history)


class LayoutConvexPoly(LayoutStrategy):
    def optimize_layout(self, graph, output_number, quality):
        region = graph.regions[0]
        radius = min(*graph.dimensions) * 0.4
        n = len(graph.graph)
        graph_set = self.initialise_graph_set(graph, n ** 2)
        for i in range(n):
            for j in range(n):
                g = graph_set[i * n + j]
                angle_offset = math.pi * j / (2 * n)
                positions = region.uniform_layout(radius, permutation = i, angle_offset = angle_offset)
                for node_id, pos in positions.items():
                    g.set_node_position(node_id, pos)
                g.recentre_nodes()
        best_graphs = list(sorted(graph_set, key = lambda x : x.energy()))
        if output_number > len(best_graphs):
            warn('%s candidate diagrams were requested, but only %s are available' % (output_number, len(best_graphs)))
        k = min(output_number, len(best_graphs))
        result_graphs = best_graphs[0:k]
        self.print_progress(1, 1)
        return (result_graphs, [best_graphs[0]])
