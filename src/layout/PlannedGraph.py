from src.layout.Label import Label
import random, math, copy, numpy as np
from numpy import arccos, dot, pi, cross
from numpy.linalg import norm
import sys
import networkx as nx

def nan_check(array):
    # if DEBUG:
    if np.any(np.isnan(array)):
        raise Exception('NaN encountered')

def round_dp(x, dp):
    y = 10 ** dp
    return round(x * y) / y

def round_precision(x, precision):
    return round(x / precision) * precision

def clamp_dot(x, y):
    return np.minimum(1, np.maximum(-1, dot(x, y)))

def distance_segment_point(A, B, P):
    if all(A == P) or all(B == P):
        return 0
    if all(A == B):
        return norm(P - A)
    if arccos(clamp_dot((P - A) / norm(P - A), (B - A) / norm(B - A))) > pi / 2:
        return norm(P - A)
    if arccos(clamp_dot((P - B) / norm(P - B), (A - B) / norm(A - B))) > pi / 2:
        return norm(P - B)
    return norm(cross(A-B, A-P))/norm(B-A)

class Vertex:
    def __init__(self, node_name, label = None):
        self.node_name = node_name
        self.label = Label(label) if label != None else Label(node_name, latex = True)

    def set_label(self, label_text):
        self.label = Label(label_text)
    
    def set_label_size(self, size):
        self.label.label_size = np.array(size)


class Edge:
    def __init__(self, edge_id, start, end, label = None, styles = None):
        self.edgeId = edge_id
        self.start = start
        self.end = end
        self.styles = [] if styles == None else styles
        self.auto_styles = []
        if label != None:
            self.set_label(label)
        else:
            self.label = Label(edge_id, latex = True, edge_label = True)
    
    def add_auto_style(self, style):
        if not style.conflicts(self.styles):
            self.auto_styles.append(style)
    
    def has_alternatives(self):
        return any(s.has_alternatives() for s in self.auto_styles)
        
    def get_styles(self):
        styles = self.styles + self.auto_styles
        return list(map(lambda x : x.style, styles))

    def set_label(self, label_text):
        self.label = Label(label_text, edge_label = True)
    
    def set_label_size(self, size):
        self.label.label_size = np.array(size)


def ccw(A, B, C):
    (Ax, Ay) = A
    (Bx, By) = B
    (Cx, Cy) = C
    return (Cy - Ay) * (Bx - Ax) > (By - Ay) * (Cx - Ax)

def intersect(A, B, C, D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


def nodesSortedByAngles(nodes, centre):
    angles = list(map(lambda x : (x, math.degrees(math.atan2(x.y - centre.y, x.x - centre.x))), nodes))
    return sorted(angles, key=lambda x : x[1])

BIG_NUMBER = 1000

class PlannedGraph:
    def __init__(self, graph, regions, dimensions):
        self.dimensions = dimensions
        self.graph = graph
        self.regions = regions
        self.node_data = graph.nodes.data('data')
        self.node_positions = graph.nodes.data('pos')
        self.reset_node_probabilities()
        self.edge_data = graph.edges(data = 'data', keys = True)
        self.angleValues = []

        dimX, dimY = self.dimensions
        n = len(self.graph)
        self.quantization = (dimX / n, dimY / n)

        node_list = [node_id for node_id, _ in self.node_data]
        self.node_indices = {node_list[i]: i for i in range(len(node_list))}
        self.reset_cache()
        
    def get_positions(self):
        return dict(self.node_positions)
    
    def get_np_positions(self):
        return np.array([pos for _, pos in self.node_positions])
    
    def set_node_position(self, node_id, position, graph = None):
        graph = graph if graph != None else self.graph
        graph.nodes[node_id]['pos'] = np.array(position)
        self.reset_cache()
    
    def reset_cache(self):
        self._energy = None
        self._energy_stats = None
        self.recompute_node_distances()
        self.recompute_edge_endpoints()
        self.recompute_region_label_positions()
    
    def recompute_node_distances(self):
        L = 2
        pos_array = self.get_np_positions()
        diff = abs(pos_array[:, np.newaxis] - pos_array) ** L
        self.pairwise_node_distances = diff.sum(axis = 2)
    
    def recompute_edge_endpoints(self):
        pos = self.node_positions
        egde_array = np.array([(pos[start], pos[end]) for start, end, _, _ in self.edge_data])
        self.edge_endpoints = egde_array
    
    def recompute_region_label_positions(self):
        for r in self.regions:
            r.compute_label_position(self.graph)
    
    def reset_node_probabilities(self):
        self.node_probabilities = {node_id: 1 for node_id in self.graph.nodes}
        return self.node_probabilities
    
    def increase_node_probability(self, node_id, amount):
        self.node_probabilities[node_id] *= amount
    
    def quantize_position(self, x, y):
        (quant_x, quant_y) = self.quantization
        new_x = round_precision(x, quant_x)
        new_y = round_precision(y, quant_y)
        return (new_x, new_y)
    
    def random_plan(self):
        (width, height) = self.dimensions
        for node_id, _ in self.node_data:
            x = width * (random.random() - 0.5)
            y = height * (random.random() - 0.5)
            (x, y) = self.quantize_position(x, y)
            self.set_node_position(node_id, (x, y))
    
    def copy(self):
        graph = self.graph.copy()
        return PlannedGraph(graph, self.regions, self.dimensions)
    
    def choose_random_node(self):
        items = self.node_probabilities.items()
        caius = [x for x, _ in items]
        values = np.fromiter((x for _, x in items), dtype = float)
        distribution = values / values.sum()
        return np.random.choice(caius, p = distribution)
    
    def random_neighbour(self, radius):
        planned_graph = self.copy()
        node_id = planned_graph.choose_random_node()
        (x, y) = planned_graph.node_positions[node_id]
        dx = radius * (random.random() * 2 - 1)
        dy = radius * (random.random() * 2 - 1)
        dxQ, dyQ = planned_graph.quantize_position(dx, dy)
        if dxQ > 0 and dyQ > 0:
            dx, dy = dxQ, dyQ
        newX = x + dx
        newY = y + dy
        planned_graph.set_node_position(node_id, (newX, newY))
        return planned_graph
    
    def apply_spring_layout(self):
        # width, height = self.dimensions
        # node_distance = math.sqrt(width ** 2 + height ** 2)
        # positions = nx.spring_layout(self.graph, k = node_distance)
        positions = nx.spring_layout(self.graph)
        for node_id, (x, y) in positions.items():
            self.set_node_position(node_id, (x, y))
    
    def recentre_nodes(self):
        n = len(self.node_positions)
        offsetX, offsetY = self.get_np_positions().sum(axis = 0) / n

        rounding_precision = 5
        for node_id, (x, y) in self.node_positions:
            newX = round_dp(x - offsetX, rounding_precision)
            newY = round_dp(y - offsetY, rounding_precision)
            self.set_node_position(node_id, (newX, newY))
    
    def energy(self):
        if self._energy != None:
            return self._energy
        self.reset_node_probabilities()
        self._energy = sum(self.energy_stats().values())
        return self._energy
    
    def energy_stats(self):
        if self._energy_stats != None:
            return self._energy_stats
        self._energy_stats = {
            'node-dist': 1500 * self.node_distances(),
            'border-dist': 10 * self.border_distance(),
            'edge-lengths': 2 * self.edge_lengths(),
            'sharp-angles': 5000 * self.sharp_angles(),
            'edge-diffs': 10 * self.edge_differences(),
            'horizontalness': 200 * self.horizontalness(),
            'node-edge-dists': 25 * self.node_edge_distances(),
            'edge-crossings': 200000 * self.edge_intersections(),
            'arrow-dirs': 10 * self.overall_arrow_direction(),
            'label-overlaps': 500 * self.label_overlaps(),
            'edge-label-overlaps': 500 * self.edge_label_overlaps()
        }
        return self._energy_stats
        
    def node_distance_sq(self, start_id, end_id):
        i = self.node_indices[start_id]
        j = self.node_indices[end_id]
        return self.pairwise_node_distances[i, j]
        
    def node_distances(self):
        ceiling = BIG_NUMBER
        # d2 = self.pairwise_node_distances
        # d2 = np.triu(1 / d2, k = len(self.node_data) % 2)
        # d2 = np.minimum(d2, ceiling)
        # np_total = d2.sum()
        # return np_total
        # A = 1
        L = 2
        total = 0
        m = 0
        region_positions = [region.label_position for region in self.regions if not region.label.empty()]
        nodeValues = list(self.get_positions().values()) + region_positions
        for i in range(len(nodeValues)):
            for j in range(i + 1, len(nodeValues)):
                (x1, y1) = nodeValues[i]
                (x2, y2) = nodeValues[j]
                d2 = abs(x2 - x1) ** L + abs(y2 - y1) ** L
                if d2 > 0:
                    m = max(m, 1 / d2)
                    total += 1 / d2
                else:
                    total += ceiling
        # print(m)
        return total
    
    def border_distance(self):
        (width, height) = self.dimensions
        positionValues = self.get_positions().values()
        (minX, _) = min(positionValues, key = lambda xy: xy[0])
        (maxX, _) = max(positionValues, key = lambda xy: xy[0])
        (_, minY) = min(positionValues, key = lambda xy: xy[1])
        (_, maxY) = max(positionValues, key = lambda xy: xy[1])
        graphWidth = maxX - minX
        graphHeight = maxY - minY
        if graphHeight >= height or graphWidth >= width:
            return math.inf
        # else:
        #     return 0
        dx2 = (width - graphWidth) ** 2
        dy2 = (height - graphHeight) ** 2
        return 1 / dx2 + 1 / dy2
    
    def edge_lengths(self):
        total = 0
        for (start, end, _, _) in self.edge_data:
            d2 = self.node_distance_sq(start, end) # some adjustment factor for individual edges
            p = 1 + math.sqrt(d2) / 16
            self.increase_node_probability(start, p)
            self.increase_node_probability(end, p)
            total += d2
        return total

    def edge_differences(self):
        total = 0
        edges = list(self.edge_data)
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                (startA, endA, _, _) = edges[i]
                (startB, endB, _, _) = edges[j]
                length1 = self.node_distance_sq(startA, endA)
                length2 = self.node_distance_sq(startB, endB)
                total += abs(math.sqrt(length1) - math.sqrt(length2)) # some adjustment factor for individual edges
        return total
    
    def node_edge_distances(self):
        total = 0
        for node_id, _ in self.node_data:
            for (start, end, _, _) in self.edge_data:
                if node_id != start and node_id != end and start != end:
                    p1 = self.node_positions[start]
                    p2 = self.node_positions[end]
                    node_pos = self.node_positions[node_id]
                    d2 = distance_segment_point(p1, p2, node_pos)
                    if d2 == 0:
                        total += BIG_NUMBER
                    else:
                        total += 1 / d2
        return total

    def sharp_angles(self):
        total = 0
        sharpness_threshold = math.pi / 6
        k = math.pi / (2 * sharpness_threshold)
        for node_id, _ in self.node_data:
            position = self.node_positions[node_id]
            in_edges = self.graph.in_edges(node_id)
            out_edges = self.graph.out_edges(node_id)
            edges = list(in_edges) + list(out_edges)
            neighbour_nodes = map(lambda x : x[0] if x[0] != node_id else x[1], edges)
            neighbour_offsets = map(lambda x : self.node_positions[x] - position, neighbour_nodes)
            neighbour_angles = list(map(lambda x : math.atan2(x[1], x[0]), neighbour_offsets))
            for i in range(len(neighbour_angles)):
                for j in range(i + 1, len(neighbour_angles)):
                    angle1 = neighbour_angles[i]
                    angle2 = neighbour_angles[j]
                    difference = abs(angle1 - angle2)
                    difference = min(difference, 2 * math.pi - difference)
                    if difference < sharpness_threshold:
                        rating = math.cos(difference * k) ** 2
                        total += rating
                        self.increase_node_probability(node_id, 1 + rating)
        return total

    def horizontalness(self):
        with np.errstate(all = 'ignore'):
            diff = abs(self.edge_endpoints[:, 1] - self.edge_endpoints[:, 0])
            lengths = diff[:, 1] ** 2 + diff[:, 0] ** 2
            gradients_x = np.nan_to_num(diff[:, 1] / diff[:, 0], nan = 0)
            gradients_y = 1 / gradients_x
            a = np.minimum(gradients_x, gradients_y) * lengths
            allow_diagonal = len(self.graph) >= 3
            gradients = None
            if allow_diagonal:
                gradients = np.nan_to_num(2 * np.sqrt(a * (1 - a)), nan = 0)
            else:
                gradients = np.nan_to_num(np.sqrt(a), nan = 0)
            nan_check(gradients)
            total = gradients.sum()
            return total
    
    def edge_intersections(self):
        total = 0
        edges = list(self.edge_data)
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                (startA, endA, _, _) = edges[i]
                (startB, endB, _, _) = edges[j]
                if startA != startB and startA != endB and startB != endA and endB != endA:
                    startAPos = self.node_positions[startA]
                    startBPos = self.node_positions[startB]
                    endAPos = self.node_positions[endA]
                    endBPos = self.node_positions[endB]
                    if intersect(startAPos, endAPos, startBPos, endBPos):
                        total += 1
                        for node_id in [startA, endA, startB, endB]:
                            self.increase_node_probability(node_id, 1.5)
        return total
    
    def label_overlaps(self):
        positions = self.get_np_positions()
        labels = np.array([node.label.label_size for _, node in self.node_data])
        concat = lambda x, y : np.concatenate((x, y), axis = 1)
        label_offsets = concat(-labels / 2, labels / 2)
        label_boxes = concat(positions, positions) + label_offsets

        # TODO finish vectorizing this stuff below
        total = 0
        for i in range(len(label_boxes)):
            for j in range(i + 1, len(label_boxes)):
                l1x, l1y, r1x, r1y = label_boxes[i]
                l2x, l2y, r2x, r2y = label_boxes[j]
                if l1x < r2x and l2x < r1x and l1y > r2y and l2y > r1y:
                    total += 1
        return total
    
    def edge_label_overlaps(self):
        # TODO vectorize this
        total = 0
        for node_id, node in self.node_data:
            pos = self.node_positions[node_id]
            label_offset = node.label.label_size / 2
            label_offset_T = node.label.label_size / 2 * np.array((1, -1))
            l = (pos - label_offset, pos - label_offset_T)
            r = (pos + label_offset, pos + label_offset_T)
            t = (pos - label_offset, pos + label_offset_T)
            b = (pos + label_offset, pos - label_offset_T)
            for start, end, _, _ in self.edge_data:
                if node_id != start and node_id != end:
                    edge_points = (self.node_positions[start], self.node_positions[end])
                    if intersect(*l, *edge_points) or intersect(*r, *edge_points) or intersect(*t, *edge_points) or intersect(*b, *edge_points):
                        total += 1
        return total
    
    def overall_arrow_direction(self):
        directions = self.edge_endpoints[:, 1] - self.edge_endpoints[:, 0]
        x, y = directions.sum(axis = 0)
        angle = math.atan2(y, x)
        magnitude = x ** 2 + y ** 2
        rating = 0
        if abs(angle) > math.pi / 2:
            rating = magnitude * math.cos(angle) ** 2
        elif angle > 0:
            rating = magnitude * math.sin(angle) ** 2
        return rating
    