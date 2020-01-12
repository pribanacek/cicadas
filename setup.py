from setuptools import setup, find_packages

setup(
    name = 'CURTIS',
    version = '0.1',
    description = 'Automatic generation of commutative diagrams',
    url = 'https://github.com/pribanacek/Part-II-Project',
    author = 'Jakub Priban',
    # license = 'something',
    packages = find_packages('antlr', 'networkx', 'numpy')
)
