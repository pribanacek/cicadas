import os, subprocess, errno
from subprocess import CalledProcessError
from src.util.Exceptions import LatexException

LATEX_PREFIX = '''\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz-cd, amsmath}
\\usetikzlibrary{decorations.pathmorphing}
\\begin{document}
\\begin{equation*}
'''

LATEX_SUFFIX = '''\\end{equation*}
\\end{document}
'''

def generateTex(tex, filepath):
    with open(filepath + '.tex', 'w+', encoding='utf-8') as f:
        f.write(tex)

def generatePDF(tex, filepath, compiler_args = []):
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

    texFile = LATEX_PREFIX + tex + LATEX_SUFFIX
    generateTex(texFile, filepath)
    command = ['pdflatex', '--interaction=nonstopmode', basename + '.tex']
    try:
        subprocess.check_output(command)
    except CalledProcessError as e:
        os.remove(basename + '.aux')
        os.chdir(cur_dir)
        raise LatexException('process failed when compiling LaTeX output', e.output.decode('ascii'))

    os.remove(basename + '.aux')
    os.remove(basename + '.log')
    os.chdir(cur_dir)
