import os, subprocess, errno

LATEX_PREFIX = '''
\\documentclass{article}
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
    subprocess.check_output(command) # check output here
    os.remove(basename + '.tex')  # Remove generated tex file
    os.chdir(cur_dir)
