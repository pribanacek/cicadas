import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('file',
    help = 'the input file to be parsed',
)

arg_parser.add_argument('-o',
    help = 'output destination (will generate a .pdf and a .tex file of that name). Default = \'./output\'',
    action = 'store',
    required = False,
    default = './output'
)

arg_parser.add_argument('-n',
    help = 'output the best N candidate diagrams. Default = 1',
    action = 'store',
    type = int,
    required = False,
    default = 1
)

arg_parser.add_argument('-p', '--preview',
    help = 'automatically open generated pdf in the web browser when finished',
    action = 'store_true', required = False
)

arg_parser.add_argument('--suppress-warnings',
    help='suppresses warnings',
    action = 'store_true', required = False
)
