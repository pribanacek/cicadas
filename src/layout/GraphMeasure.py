import os, subprocess, errno, re

LATEX_PREFIX = '''
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz-cd, amsmath}
\\usetikzlibrary{decorations.pathmorphing}
\\begin{document}
stuff
'''
# TODO add configurations to prefix here

LATEX_SUFFIX = '''\\end{document}
'''

WIDTH = 'width'
HEIGHT = 'height'

def getNodeCode(node):
    nodeId = node.nodeId
    label = node.label
    lines = [
        '\\begin{tikzpicture}',
        '\\node (' + nodeId + ') at (0, 0) {' + label + '};',
        '\\end{tikzpicture}'
    ]
    return '\n'.join(lines)

def getNodeMeasurementCode(node):
    nodeId = node.nodeId
    nodeLatex = getNodeCode(node)
    lines = [
        '\\newlength{\\height' + nodeId + '}',
        '\\newlength{\\width' + nodeId + '}',
        '\\settoheight{\\height' + nodeId + '}{\\hbox{' + nodeLatex + '}}',
        '\\settowidth{\\width' + nodeId + '}{\\hbox{' + nodeLatex + '}}',
        '\\wlog{' + WIDTH + ' ' + nodeId + '}\\showthe\\width' + nodeId,
        '\\wlog{' + HEIGHT + ' ' + nodeId + '}\\showthe\\height' + nodeId
    ]
    return lines

def getMeasurementLatex(nodeData):
    lines = [LATEX_PREFIX]
    for node in nodeData.values():
        lines = lines + getNodeMeasurementCode(node)
    lines.append(LATEX_SUFFIX)
    return '\n'.join(lines)

def measureNodes(nodeData):
    measurements = {}
    latex = getMeasurementLatex(nodeData)
    filepath = './temp'
    logs = generateLatexLog(latex, filepath)
    for line in logs:
        (dim, nodeId, _, value, _unit) = line
        if not nodeId in measurements:
            measurements[nodeId] = [0, 0]
        if dim == WIDTH:
            measurements[nodeId][0] = float(value)
        elif dim == HEIGHT:
            measurements[nodeId][1] = float(value)

    for nodeId, dimensions in measurements.items():
        nodeData[nodeId].dimensions = tuple(dimensions)

    return measurements

def generateLatexLog(latex, filepath):
    cur_dir = os.getcwd()
    dest_dir = os.path.dirname(filepath)
    basename = os.path.basename(filepath)
    if basename == '':
        basename = 'default_basename'
    try:
        os.chdir(dest_dir)
    except:
        print('Couldn\'t change directory to ' + dest_dir)
        os.chdir(cur_dir)

    fileTex = filepath + '.tex'
    with open(fileTex, 'w+', encoding='utf-8') as f:
        f.write(latex)

    command = ['pdflatex', '-draftmode', '--interaction=nonstopmode', fileTex]
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        print('Process returned code', e.returncode)
        # print(e.output)

    output = None
    TYPE = '(' + WIDTH + '|' + HEIGHT + ')'
    ID = '([_a-zA-Z][_a-zA-Z0-9]*)'
    LENGTH = '([0-9]*\\.[0-9]+|[0-9]+)'
    UNITS = '([a-z]+)'
    with open(filepath + '.log', 'r', encoding='utf-8') as f:
        data = f.read()
        regex = re.compile(TYPE + ' ' + ID + '(\\n)+> ' + LENGTH + UNITS, re.MULTILINE)
        output = regex.findall(data)

    os.remove(fileTex)
    os.remove(filepath + '.aux')
    os.remove(filepath + '.log')
    os.chdir(cur_dir)
    return output
