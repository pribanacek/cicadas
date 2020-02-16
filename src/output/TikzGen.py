import math
from string import Template

from src.layout.PlannedGraph import PlannedGraph

BEGIN_TIKZ_PICTURE = '\\begin{tikzpicture}'
END_TIKZ_PICTURE = '\\end{tikzpicture}'

PATH_START = '\\path[commutative diagrams/.cd, every arrow, every label]'

NODE_TEMPLATE = Template('\\node ($id) at ($x, $y) {$label};')
EDGE_TEMPLATE = Template('($start) edge$styles node {$label} ($end)')


def getNodeString(nodeId, node, position):
    (x, y) = position
    return NODE_TEMPLATE.substitute(
        id = nodeId,
        x = x,
        y = y,
        label = node.label
    )

def getStylesString(styles):
    if styles == None or len(styles) < 1:
        return ''
    styleString = '['
    for style in styles:
        styleString += 'commutative diagrams/' + style + ','
    styleString = styleString[:-1] + ']'
    return styleString

def getEdgeString(start, end, edge):
    return EDGE_TEMPLATE.substitute(
        start = start,
        end = end,
        label = edge.label,
        styles = getStylesString(edge.styles)
    )

def getTikzLines(graph):
    lines = [BEGIN_TIKZ_PICTURE]
    for nodeId, node in graph.node_data:
        position = graph.node_positions[nodeId]
        lines.append(getNodeString(nodeId, node, position))
    lines.append(PATH_START)
    for start, end, _, edge in graph.edge_data:
        lines.append(getEdgeString(start, end, edge))
    lines[-1] += ';'
    lines.append(END_TIKZ_PICTURE)
    return lines

def generateTikz(graph):
    lines = getTikzLines(graph)
    return '\n'.join(lines) + '\n'
