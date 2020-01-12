import math
from string import Template

from src.layout.PlannedGraph import PlannedGraph

BEGIN_TIKZ_PICTURE = '\\begin{tikzpicture}'
END_TIKZ_PICTURE = '\\end{tikzpicture}'

PATH_START = '\\path[commutative diagrams/.cd, every arrow, every label]'

NODE_TEMPLATE = Template('\\node ($id) at ($x, $y) {$label};')
EDGE_TEMPLATE = Template('($start) edge$styles node {$label} ($end)')


def getNodeString(node):  
    return NODE_TEMPLATE.substitute(
        id = node.nodeId,
        x = node.x,
        y = node.y,
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

def getEdgeString(edge):
    return EDGE_TEMPLATE.substitute(
        start = edge.start.nodeId,
        end = edge.end.nodeId,
        label = edge.label,
        styles = getStylesString(edge.styles)
    )

def getTikzLines(graph):
    lines = [BEGIN_TIKZ_PICTURE]
    for node in graph.nodeData:
        lines.append(getNodeString(node))
    lines.append(PATH_START)
    for edge in graph.edgeData:
        lines.append(getEdgeString(edge))
    lines[-1] += ';'
    lines.append(END_TIKZ_PICTURE)
    return lines

def generateTikz(graph):
    lines = getTikzLines(graph)
    return '\n'.join(lines) + '\n'
