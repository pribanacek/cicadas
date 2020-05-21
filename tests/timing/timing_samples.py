from src.util.Exceptions import SyntaxException, ParsingException, LatexException, NotSupportedException

import src.parser.Parser as Parser
from src.output.TikzGenerator import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import time
import numpy as np


def measure_times(filename):
    n = 1
    quality = 5

    start = time.time()
    graph_assembler = Parser.parse_file('samples/' + filename)
    parse_time = time.time()

    GraphMeasure.measure(graph_assembler.nodes, graph_assembler.edges, graph_assembler.regions)
    measure_time = time.time()

    graph = graph_assembler.get_graph()
    topology_time = time.time()

    (min_graphs, _) = optimize_layout(graph, n, quality)
    layout_time = time.time()

    generate_tikz(min_graphs)
    output_time = time.time()

    dic = {
        'parsing': parse_time - start,
        'measure': measure_time - parse_time,
        'topology': topology_time - measure_time,
        'layout': layout_time - topology_time,
        'output': output_time - layout_time,
        'total': output_time - start,
    }
     
    lst = [
        parse_time - start,
        measure_time - parse_time,
        topology_time - measure_time,
        layout_time - topology_time,
        output_time - layout_time,
        output_time - start,
    ]

    return dic, lst

fdp = lambda x: "{0:0.3f}".format(x)

np.set_printoptions(formatter={'float': fdp})

def main(sample):
    samples = 25
    durations = []
    for i in range(samples):
        print('running diagram', i + 1, 'out of', samples)
        _, lst = measure_times(sample)
        durations.append(lst)
    data = np.array(durations)
    mean = np.mean(data, axis = 0)
    stdev = np.std(data, axis = 0)
    print('TIMING FOR', sample)
    total = '$' + fdp(mean[5]) + ' \\pm ' + fdp(stdev[5]) + '$'
    layout = '$' + fdp(mean[3]) + ' \\pm ' + fdp(stdev[3]) + '$'
    return (total, layout)

if __name__ == "__main__":
    output = ''
    for i in range(4, 5):
        print('running sample', i + 1)
        sample = 'sample' + str(i + 1)
        total, layout = main(sample)
        output += layout + ' & ' + total + ' \\\\\n'
    print(output)
