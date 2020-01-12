import os, sys, webbrowser

import src.parser.Parser as Parser

from src.output.TikzGen import generateTikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimizeLayout

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

if __name__ == "__main__":
    filename = sys.argv[1]
    graph = Parser.parse(filename)
    result = generateTikz(optimizeLayout(graph))
    outputPath = './thing'
    generatePDF(result, outputPath)
    fullPath = os.path.abspath(outputPath)
    webbrowser.open_new('file://' + fullPath + '.pdf')
    print(result)
    # os.system("echo '%s' | xclip -selection clipboard" % result.replace('\\', '\\\\'))
