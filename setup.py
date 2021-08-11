from setuptools import setup

with open("README.md", 'r') as file:
    long_description = file.read()

setup(
    name='treeds',
    version='0.0.1',
    description='Simple implementation of Tree Data Structure',
    long_description_content_type="text/markdown",
    long_description=long_description,
    py_modules=['treeds'],
    package_dir={'': 'src'},
    keywords=['python', 'treeds', 'tree python', 'data structure', 'tree data structure', 'pytree'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
