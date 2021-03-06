from setuptools import setup, find_packages

setup(
    name="cicadas",
    version="1.0.0a2",
    author="Jakub Priban",
    author_email="jp775@cam.ac.uk",
    description="Self-constructing commutative diagrams",
    long_description_content_type="text/markdown",
    url="https://github.com/pribanacek/cicadas",
    packages=find_packages(where = 'src'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/pribanacek/cicadas/issues',
        'Source': 'https://github.com/pribanacek/cicadas',
    },
    install_requires=[
        'numpy>=1.17.4',
        'antlr4-python3-runtime==4.7.2',
        'networkx>=2.4'
    ]
)
