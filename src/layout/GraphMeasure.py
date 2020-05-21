import os, subprocess, errno, re
from src.util.Exceptions import LatexException

LATEX_PREFIX = '''
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz-cd, amsmath, printlen}
\\usetikzlibrary{decorations.pathmorphing}
\\begin{document}
stuff
'''

LATEX_SUFFIX = '''\\end{document}
'''

WIDTH = 'width'
HEIGHT = 'height'

CHAR_OFFSET = 65

def encode_index(i):
    chars = list(map(lambda x : chr(int(x) + CHAR_OFFSET), str(i)))
    return ''.join(chars)

def decode_index(a):
    digits = list(map(lambda x : str(ord(x) - CHAR_OFFSET), a))
    return int(''.join(digits))

def get_label_code(label):
    text = label.text
    if label.font_size != None:
        return '\\fontsize{' + label.font_size + '}{1pt}{' + text + '}'
    if label.edge_label:
        return '\\scriptsize{' + text + '}'
    return '\\normalsize{' + text + '}'

def get_measurement_code(label_id, label):
    node_latex = get_label_code(label)
    lines = [
        '\\newlength{\\height' + label_id + '}',
        '\\newlength{\\width' + label_id + '}',
        '\\settoheight{\\height' + label_id + '}{\\hbox{' + node_latex + '}}',
        '\\settowidth{\\width' + label_id + '}{\\hbox{' + node_latex + '}}',
        '\\wlog{' + WIDTH + ':' + label_id + '\\printlength{\\width' + label_id + '}}'
        '\\wlog{' + HEIGHT + ':' + label_id + '\\printlength{\\height' + label_id + '}}'
    ]
    return lines

def get_measurement_latex(label_data):
    lines = [LATEX_PREFIX]
    for label_id, label in label_data.items():
        if len(label.text) > 0:
            lines = lines + get_measurement_code(label_id, label)
    lines.append(LATEX_SUFFIX)
    return '\n'.join(lines)

def generate_label_dict(labels):
    label_data = {}
    for i in range(len(labels)):
        x = encode_index(i)
        label_data[x] = labels[i]
    return label_data

def measure_labels(labels):
    pt_to_cm = 1 / 28.45724
    label_dict = generate_label_dict(labels)
    latex = get_measurement_latex(label_dict)
    filepath = './temp'
    logs = generate_latex_log(latex, filepath)
    for line in logs:
        (dim, label_id, value, _unit) = line
        if dim == WIDTH:
            width = float(value) * pt_to_cm
            label_dict[label_id].set_label_width(width)
        elif dim == HEIGHT:
            height = float(value) * pt_to_cm
            label_dict[label_id].set_label_height(height)

def measure(nodes, edges, regions):
    label_list = lambda l : list(map(lambda x : x.label, l))
    labels = label_list(nodes.values()) + label_list(edges.values()) + label_list(regions)
    measure_labels(labels)

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

    file_tex = filepath + '.tex'
    with open(file_tex, 'w+', encoding='utf-8') as f:
        f.write(latex)

    command = ['pdflatex', '-draftmode', '--interaction=nonstopmode', file_tex]
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        os.remove(filepath + '.tex')
        os.remove(filepath + '.aux')
        os.chdir(cur_dir)
        raise LatexException('process failed when measuring subcomponents', e.output.decode('ascii'))

    output = None
    TYPE = '(' + WIDTH + '|' + HEIGHT + ')'
    ID = '([_a-zA-Z][_a-zA-Z0-9]*)'
    LENGTH = '([0-9]*\\.[0-9]+|[0-9]+)'
    UNITS = '([a-z]+)'
    SEP = '(\\\\def ' + UNITS + '{' + UNITS + '})'
    with open(filepath + '.log', 'r', encoding='utf-8') as f:
        data = f.read()
        regex = re.compile(TYPE + ':' + ID + SEP + LENGTH + UNITS, re.MULTILINE)
        output = list(map(lambda x : (x[0], x[1], x[5], x[6]), regex.findall(data)))
    os.remove(file_tex)
    os.remove(filepath + '.aux')
    os.remove(filepath + '.log')
    os.chdir(cur_dir)
    return output
