from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A Graph Data Structure with many useful methods'
LONG_DESCRIPTION = 'A package that allows to use Graph Data Structure to perform many tasks.'

# Setting up
setup(
    name="graph",
    version=VERSION,
    author="Tatwik",
    author_email="<sreenu143anupama@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'graph', 'data-structure', 'search', 'algorithms', 'bfs', 'dfs', 'a*', 'heuristic'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ]
)
