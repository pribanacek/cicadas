import os, sys, webbrowser

import src.parser.Parser as Parser

from src.output.TikzGen import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import networkx as nx

import src.tests.LayoutOptimisation
import src.tests.TikzGeneration

import src.visualisation.animate as animate_graphs

# def runTest(test):   
#     testName = sys.argv[1]
#     test = eval('Test' + testName) # this is unsafe
#     if callable(test):
#         result = test()
#         print(result)
#     else:
#         print('Unknown test ' + test)

# def layoutTest(test):
#     if len(sys.argv) < 2:
#         print('Please specify a test')
    
#     testName = sys.argv[1]
#     test = eval('Test' + testName) # this is unsafe
#     if callable(test):
#        result = test()
#        path = '/home/jacob/Cambridge/Part_II_Project/Part-II-Project/thing'
#        generatePDF(result, path)
#        webbrowser.open_new('file://' + path + '.pdf')
#        print(result)
#        os.system("echo '%s' | xclip -selection clipboard" % result.replace('\\', '\\\\'))
#     else:
#         print('Unknown test ' + test)

import cProfile

def main(filename):
    graph_assembler = Parser.parse(filename)
    GraphMeasure.measure(graph_assembler.nodes, graph_assembler.edges, graph_assembler.regions)
    graph = graph_assembler.getGraph()
    (minGraph, graphs) = optimize_layout(graph)

    animate_graphs.start_animation_thread(graphs)

    result = generate_tikz(minGraph)

    outputPath = './thing'
    generatePDF(result, outputPath)
    fullPath = os.path.abspath(outputPath)
    webbrowser.open_new('file://' + fullPath + '.pdf')
    # os.remove(fullPath + '.pdf')
    print(result)


if __name__ == "__main__":
    filename = sys.argv[1]
    # cProfile.run('main(filename)')
    main(filename)
