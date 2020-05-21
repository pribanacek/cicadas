from src.util.Exceptions import SyntaxException, ParsingException, LatexException, NotSupportedException

import src.parser.Parser as Parser
from src.output.TikzGenerator import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import time
import numpy as np


def measure_times(candidates, iterations):
    start = time.time()
    graph_assembler = Parser.parse_file('samples/sample5')
    parse_time = time.time()

    GraphMeasure.measure(graph_assembler.nodes, graph_assembler.edges, graph_assembler.regions)
    measure_time = time.time()

    graph = graph_assembler.get_graph()
    topology_time = time.time()

    (min_graphs, _) = optimize_layout(graph, candidates, iterations)
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

def main(candidates, iterations):
    samples = 5
    durations = []
    for i in range(samples):
        print('running diagram', i + 1, 'out of', samples)
        _, lst = measure_times(candidates, iterations)
        durations.append(lst)
    data = np.array(durations)
    mean = np.mean(data, axis = 0)
    stdev = np.std(data, axis = 0)
    output = str(iterations) + '\t' + fdp(mean[5]) + '\t' + fdp(stdev[5]) + '\t0 \n'
    return output

if __name__ == "__main__":
    output = ''
    for i in range(20):
        print('running sample', i + 1)
        candidates = 1
        iterations = 100 * (i + 1)
        line = main(candidates, iterations)
        output += line
    print(output)
