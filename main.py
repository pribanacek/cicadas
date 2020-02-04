import os, sys, webbrowser

import src.parser.Parser as Parser

from src.output.TikzGen import generateTikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimizeLayout
import src.layout.GraphMeasure as GraphMeasure

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import src.tests.LayoutOptimisation
import src.tests.TikzGeneration

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

def plotGraph(fig, graphs, i):
    graph = graphs[i]
    fig.clear()
    pos = graph.getPositions()
    nx.draw(graph.graph, pos)

if __name__ == "__main__":
    filename = sys.argv[1]
    graphAssembler = Parser.parse(filename)
    GraphMeasure.measureNodes(graphAssembler.nodes)
    graph = graphAssembler.getGraph()
    (minGraph, graphs) = optimizeLayout(graph)
    result = generateTikz(minGraph)

    outputPath = './thing'
    generatePDF(result, outputPath)
    fullPath = os.path.abspath(outputPath)
    webbrowser.open_new('file://' + fullPath + '.pdf')

    print(result)

    animate = False
    if animate:
        fig = plt.figure()
        update = lambda i : plotGraph(fig, graphs, i)
        ani = animation.FuncAnimation(fig, update, frames=len(graphs), interval=100, repeat=False)
        plt.show()

    # os.system("echo '%s' | xclip -selection clipboard" % result.replace('\\', '\\\\'))
