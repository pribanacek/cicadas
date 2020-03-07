import argparse

DESCRIPTION = 'CICADAS description.'

arg_parser = argparse.ArgumentParser(description = 'CICADAS description')

arg_parser.add_argument('filename',
    help = 'the input file to be parsed',
)

arg_parser.add_argument('-o',
    help = 'output destination (will generate a .pdf and a .tex file of that name). Default: \'./output\'',
    action = 'store',
    required = False,
    default = './output'
)

arg_parser.add_argument('-n',
    help = 'number of candidate diagrams to generate',
    action = 'store',
    type = int,
    required = False,
    default = 1
)

arg_parser.add_argument('-q', '--quality',
    help = 'adjust running time to affect quality. acceptable are integers > 0. default = 5',
    action = 'store',
    type = int,
    required = False,
    default = 5
)

# arg_parser.add_argument('-s', '--strategy',
#     help = 'layout strategy to use',
#     action = 'store',
#     type = int,
#     required = False,
#     default = 0
# )

arg_parser.add_argument('-p', '--preview',
    help = 'automatically open generated pdf when finished',
    action = 'store_true', required = False
)

arg_parser.add_argument('-c', '--auto-clipboard',
    help = 'automatically copy tikz output to clipboard',
    action = 'store_true', required = False
)

# arg_parser.add_argument('--silent',
#     help = 'suppress all messages',
#     action = 'store_true', required = False
# )

arg_parser.add_argument('--suppress-warnings',
    help='suppresses warnings',
    action = 'store_true', required = False
)
