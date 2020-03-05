import os, sys, webbrowser

from src.util.Exceptions import SyntaxException, ParsingException, LatexException

import src.parser.Parser as Parser

from src.output.TikzGen import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import networkx as nx

import src.tests.LayoutOptimisation
import src.tests.TikzGeneration

import src.visualisation.animate as animate_graphs

import cProfile


def main(filename):
    graph_assembler = Parser.parse(filename)
    GraphMeasure.measure(graph_assembler.nodes, graph_assembler.edges, graph_assembler.regions)
    graph = graph_assembler.getGraph()
    (min_graph, graphs) = optimize_layout(graph)

    animate_graphs.start_animation_thread(graphs)

    result = generate_tikz(min_graph)

    outputPath = './thing'
    generatePDF(result, outputPath)
    full_path = os.path.abspath(outputPath)
    webbrowser.open_new('file://' + full_path + '.pdf')
    # os.remove(fullPath + '.pdf')
    print(result)


if __name__ == "__main__":
    filename = sys.argv[1]
    # cProfile.run('main(filename)')

    try:
        main(filename)
    except FileNotFoundError as e:
        print(e)
    except ParsingException as e:
        message = 'Error occurred when parsing file'
        if e.position != None:
            message += ' at line ' + e.position
        print(message, e, sep = '\n')
    except LatexException as e:
        message = 'Error occurred when compiling LaTeX'
        print('LaTeX error:', e)
