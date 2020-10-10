import pathlib
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the version from the VERSION file
version = (here / 'VERSION').read_text(encoding='utf-8')

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="python-fx",
    version=version,
    author="Yutian Wu",
    author_email="yutianwu@umich.edu",
    description="A python-native fx-alike terminal JSON viewer with JSONPath Integration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cielong/pyfx",
    license="MIT",
    keywords="fx, pyfx, json viewer, tui",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=[
        'click',
        'urwid',
        'overrides',
        'jsonpath-ng'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={
        "console_scripts": ["pyfx=pyfx.cli:main"]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ],
    python_requires=">=3.8"
)
