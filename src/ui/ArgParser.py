import argparse

DESCRIPTION = 'CICADAS description.'

arg_parser = argparse.ArgumentParser(description = 'CICADAS description')

arg_parser.add_argument('filename',
    help = 'the input file to be parsed'
)

arg_parser.add_argument('-n',
    help = 'number of candidate diagrams to generate',
    action = 'store', required = False
)

arg_parser.add_argument('-s', '--strategy',
    help = 'layout strategy to use',
    action = 'store', required = False
)

arg_parser.add_argument('-d', '--auto-display-pdf',
    help = 'automatically copy output to clipboard',
    action = 'store_true', required = False
)

arg_parser.add_argument('-ac', '--auto-clipboard',
    help = 'automatically copy output to clipboard',
    action = 'store_true', required = False
)

arg_parser.add_argument('--silent',
    help = 'suppress all messages',
    action = 'store_true', required = False
)

arg_parser.add_argument('--suppress-warnings',
    help='suppresses warnings',
    action = 'store_true', required = False
)
