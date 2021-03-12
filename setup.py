import pathlib
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()


def get_version(version_file):
    about = {}
    with open(version_file, 'r') as fp:
        exec(fp.read(), about)
    return about["__version__"]


# get the version from the __version__.py file
version = get_version("src/pyfx/__version__.py")

# get the long description from the README file
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
    package_data={'pyfx': [
        # pyfx config files
        'config/*.yml',
        # antlr4 related files
        'mode/common/jsonpath/*.g4',
        'mode/common/jsonpath/*.interp',
        'mode/common/jsonpath/*.tokens',
        # predefined key mappers
        'view/keymapper/modes/*.yml'
    ]},
    include_package_data=True,
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=[
        'click',
        'urwid',
        'overrides',
        'jsonpath-ng',
        'loguru',
        'yamale',
        'dataclasses',
        'dacite',
        'first',
        'pyperclip',
        'antlr4-python3-runtime==4.8'
    ],
    extras_require={
        'test': [
            'pytest-runner',
            'parameterized'
        ]
    },
    entry_points={
        "console_scripts": ["pyfx=pyfx.cli:main"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ],
    python_requires=">=3.8"
)
