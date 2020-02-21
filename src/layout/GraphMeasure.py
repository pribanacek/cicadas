import os, subprocess, errno, re

LATEX_PREFIX = '''
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz-cd, amsmath, printlen}
\\usetikzlibrary{decorations.pathmorphing}
\\begin{document}
stuff
'''
# TODO add configurations to prefix here

LATEX_SUFFIX = '''\\end{document}
'''

WIDTH = 'width'
HEIGHT = 'height'

def get_node_code(node):
    node_name = node.node_name
    label = node.label
    lines = [
        '\\begin{tikzpicture}',
        '\\node (' + node_name + ') at (0, 0) {' + label + '};',
        '\\end{tikzpicture}'
    ]
    return '\n'.join(lines)

def get_node_measurement_code(node):
    node_name = node.node_name
    nodeLatex = get_node_code(node)
    lines = [
        '\\newlength{\\height' + node_name + '}',
        '\\newlength{\\width' + node_name + '}',
        '\\settoheight{\\height' + node_name + '}{\\hbox{' + nodeLatex + '}}',
        '\\settowidth{\\width' + node_name + '}{\\hbox{' + nodeLatex + '}}',
        '\\wlog{' + WIDTH + ':' + node_name + '\\printlength{\\width' + node_name + '}}'
        '\\wlog{' + HEIGHT + ':' + node_name + '\\printlength{\\height' + node_name + '}}'
    ]
    return lines

def get_measurement_latex(node_data):
    lines = [LATEX_PREFIX]
    for node in node_data.values():
        lines = lines + get_node_measurement_code(node)
    lines.append(LATEX_SUFFIX)
    return '\n'.join(lines)

def measure_nodes(node_data):
    pt_to_cm = 1 / 28.45724
    measurements = {}
    latex = get_measurement_latex(node_data)
    filepath = './temp'
    logs = generate_latex_log(latex, filepath)
    for line in logs:
        (dim, node_name, value, _unit) = line
        if not node_name in measurements:
            measurements[node_name] = [0, 0]
        if dim == WIDTH:
            measurements[node_name][0] = float(value) * pt_to_cm
        elif dim == HEIGHT:
            measurements[node_name][1] = float(value) * pt_to_cm # TODO proper conversion from pt

    for node_name, dimensions in measurements.items():
        node_data[node_name].set_label_size(dimensions)

    return measurements

def generate_latex_log(latex, filepath):
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
        print('Process returned code', e.returncode) # TODO: generate a useful exception
        print(e)

    output = None
    TYPE = '(' + WIDTH + '|' + HEIGHT + ')'
    ID = '([_a-zA-Z][_a-zA-Z0-9]*)'
    LENGTH = '([0-9]*\\.[0-9]+|[0-9]+)'
    UNITS = '([a-z]+)'
    SEP = '(\\\\def ' + UNITS + '{' + UNITS + '})' # TODO take care of this mess
    with open(filepath + '.log', 'r', encoding='utf-8') as f:
        data = f.read()
        regex = re.compile(TYPE + ':' + ID + SEP + LENGTH + UNITS, re.MULTILINE)
        output = list(map(lambda x : (x[0], x[1], x[5], x[6]), regex.findall(data))) # TODO clean this up
    os.remove(fileTex)
    os.remove(filepath + '.aux')
    os.remove(filepath + '.log')
    os.chdir(cur_dir)
    return output
