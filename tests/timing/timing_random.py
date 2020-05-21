from src.util.Exceptions import SyntaxException, ParsingException, LatexException, NotSupportedException

import src.parser.Parser as Parser
from src.output.TikzGenerator import generate_tikz
from src.output.AutoRender import generatePDF
from src.layout.LayoutOptimizer import optimize_layout
import src.layout.GraphMeasure as GraphMeasure

import time
import numpy as np

def generate_polygon_diagram(size):
    composition = ' . '.join(['f . g'] * size)

    code = '''
    size 16,16
    f: A -> B
    g: B -> A
    ''' + composition + ' = ID'
    return code

def generate_diagram(size):
    region = 'g . f = g . f\n'
    code = '''
    size 16,16
    f: A -> B
    g: B -> A
    ''' + (region * size)
    return code

def measure_times(code):
    candidates = 1
    iterations = 350

    start = time.time()
    graph_assembler = Parser.parse_string(code)
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

def main(size):
    code = generate_diagram(size)
    samples = 5
    durations = []
    for i in range(samples):
        print('running sample', i + 1, 'out of', samples)
        _, lst = measure_times(code)
        durations.append(lst)
    data = np.array(durations)
    mean = np.mean(data, axis = 0)
    stdev = np.std(data, axis = 0)
    node_number = size + 3
    output = str(node_number) + '\t' + fdp(mean[5]) + '\t' + fdp(stdev[5]) + '\t0 \n'
    return output

if __name__ == "__main__":
    output = ''
    for i in range(2, 20):
        print('running size', i)
        line = main(i)
        output += line
    print(output)
