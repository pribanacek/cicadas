import os, sys, webbrowser

from src.util.Exceptions import SyntaxException, ParsingException, LatexException, NotSupportedException
from src.cli.ArgParser import arg_parser
import src.util.Logging as Logging

import src.parser.Parser as Parser

from src.output.TikzGen import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import networkx as nx

import cProfile


def main(input_file, output_path, n, preview, clipboard = False, quality = 5):
    graph_assembler = Parser.parse_file(input_file)
    GraphMeasure.measure(graph_assembler.nodes, graph_assembler.edges, graph_assembler.regions)
    graph = graph_assembler.getGraph()
    (min_graphs, graphs) = optimize_layout(graph, n, quality)

    # if os.environ['CICADAS_VIZ'] == 'True':
    #     # import src.visualisation.animate as animate
    #     # animate.start_animation_thread(graphs)
    #     import src.visualisation.interactive as interactive
    #     interactive.start_animation_thread(min_graphs[0])

    result = generate_tikz(min_graphs)
    generatePDF(result, output_path)

    if preview:
        full_path = os.path.abspath(output_path)
        webbrowser.open_new('file://' + full_path + '.pdf')
    
    print('Successfully generated diagram:\n')
    print(result)


if __name__ == "__main__":
    args = arg_parser.parse_args(sys.argv[1:]) # TODO check this off-by-one

    # cProfile.run('main(filename)')
    # if args.silent:
    #     Logging.silent = True
    if args.suppress_warnings:
        Logging.suppress_warnings = True

    try:
        main(args.file, args.o, args.n, args.preview)
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
    except PermissionError as e:
        print('Permission error occurred')
        print('Make sure you have permission to read the source, and to read and write to the destination')
    except NotSupportedException as e:
        print('Unsupported feature:', e)
    # except Exception as e:
    #     print(e)
