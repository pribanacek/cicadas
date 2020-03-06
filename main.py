import os, sys, webbrowser

from src.util.Exceptions import SyntaxException, ParsingException, LatexException
from src.ui.ArgParser import arg_parser
import src.util.Logging as Logging

import src.parser.Parser as Parser

from src.output.TikzGen import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import networkx as nx

import src.tests.LayoutOptimisation
import src.tests.TikzGeneration

import cProfile


def main(filename, output_path = './output'):
    graph_assembler = Parser.parse(filename)
    GraphMeasure.measure(graph_assembler.nodes, graph_assembler.edges, graph_assembler.regions)
    graph = graph_assembler.getGraph()
    (min_graph, graphs) = optimize_layout(graph)

    if os.environ['CICADAS_VIZ'] == 'True':
        import src.visualisation.animate as animate
        animate.start_animation_thread(graphs)

    result = generate_tikz(min_graph)

    generatePDF(result, output_path)
    full_path = os.path.abspath(output_path)
    webbrowser.open_new('file://' + full_path + '.pdf')
    # os.remove(fullPath + '.pdf')
    print(result)


if __name__ == "__main__":
    args = arg_parser.parse_args(sys.argv[1:]) # TODO check this off-by-one
    # print(vars(args))

    # cProfile.run('main(filename)')
    if args.silent:
        Logging.silent = True
    if args.suppress_warnings:
        Logging.suppress_warnings = True

    try:
        main(args.filename)
    except FileNotFoundError as e:
        print(e)
    except ParsingException as e:
        message = 'Error occurred when parsing file'
        if e.position != None:
            message += ' at line ' + e.position
        print(message, e, sep = '\n')
    except LatexException as e:
        print('Error occurred when compiling LaTeX:', e.msg)
        print('pdflatex subprocess returned the following error:')
        print(e.error)
    except Exception as e:
        print(e)
