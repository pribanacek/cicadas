import math
from string import Template

from src.layout.PlannedGraph import PlannedGraph

BEGIN_TIKZ_PICTURE = '''
\\begin{equation*}
\\begin{tikzpicture}'''

END_TIKZ_PICTURE = '''\\end{tikzpicture}
\\end{equation*}
'''

PATH_START = '\\path[commutative diagrams/.cd, every arrow, every label]'

NODE_TEMPLATE = Template('\\node ($id) at ($x, $y) {$label};')
EDGE_TEMPLATE = Template('($start) edge$styles node {$label} ($end)')


def get_node_string(node_id, label, position):
    (x, y) = position
    return NODE_TEMPLATE.substitute(
        id = node_id,
        x = x,
        y = y,
        label = label
    )

def get_styles_string(styles):
    if styles == None or len(styles) < 1:
        return ''
    styleString = '['
    for style in styles:
        styleString += 'commutative diagrams/' + style + ','
    styleString = styleString[:-1] + ']'
    return styleString

def get_edge_string(start, end, edge):
    return EDGE_TEMPLATE.substitute(
        start = start,
        end = end,
        label = edge.label,
        styles = get_styles_string(edge.get_styles())
    )

def get_tikz_code_lines(graph):
    lines = [BEGIN_TIKZ_PICTURE]
    for node_id, node in graph.node_data:
        position = graph.node_positions[node_id]
        lines.append(get_node_string(node_id, node.label, position))
    for region in graph.regions:
        if not region.label.empty():
            position = region.compute_label_position(graph.graph)
            node_id = 'region--' + str(region.region_id)
            lines.append(get_node_string(node_id, region.label, position))
    lines.append(PATH_START)
    for start, end, _, edge in graph.edge_data:
        lines.append(get_edge_string(start, end, edge))
    lines[-1] += ';'
    lines.append(END_TIKZ_PICTURE)
    return lines

def generate_tikz(graphs):
    latex_lines = []
    for graph in graphs:
        graph_tikz_code = get_tikz_code_lines(graph)
        latex_lines = latex_lines + graph_tikz_code
    return '\n'.join(latex_lines) + '\n'
