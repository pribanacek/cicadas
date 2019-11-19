import math
from string import Template
from PlannedGraph import PlannedGraph


BEGIN_TIKZ_PICTURE = '\\begin{tikzpicture}'
END_TIKZ_PICTURE = '\\end{tikzpicture}'

PATH_START = '\\path[commutative diagrams/.cd, every arrow, every label]'

NODE_TEMPLATE = Template('\\node ($id) at ($theta : $distance) {$$$label$$};')
EDGE_TEMPLATE = Template('($start) edge$styles node {$$$label$$} ($end)')


def getPolarAngle(x, y):
    return math.degrees(math.atan2(y, x))

def getPolarMagnitude(x, y):
    return math.sqrt(x * x + y * y)

def getNodeString(node):  
    return NODE_TEMPLATE.substitute(
        id = node.identifier,
        theta = getPolarAngle(node.x, node.y),
        distance = getPolarMagnitude(node.x, node.y),
        label = node.label
    )

def getStylesString(styles):
    if styles == None or len(styles) < 1:
        return ''
    else:
        styleString = '['
        for style in styles:
            styleString += 'commutative diagrams/' + style + ','
        styleString = styleString[:-1] + ']'
        return styleString

def getEdgeString(edge):  
    return EDGE_TEMPLATE.substitute(
        start = edge.start.identifier,
        end = edge.end.identifier,
        label = edge.label,
        styles = getStylesString(edge.styles)
    )

def getTikzLines(graph):
    lines = [BEGIN_TIKZ_PICTURE]
    for node in graph.nodes:
        lines.append(getNodeString(node))
    lines.append(PATH_START)
    for edge in graph.edges:
        lines.append(getEdgeString(edge))
    lines[-1] += ';'
    lines.append(END_TIKZ_PICTURE)
    return lines

def generateTikz(graph):
    lines = getTikzLines(graph)
    return '\n'.join(lines) + '\n'
