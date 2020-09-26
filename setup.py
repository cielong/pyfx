import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="pyfx",
    version="0.0.1",
    author="Yutian Wu",
    author_email="yutianwu@umich.edu",
    description="A python-native fx-alike terminal JSON viewer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cielong/pyfx",
    license="MIT",
    keywords="fx, pyfx, json viewer, tui",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'click',
        'urwid',
        'overrides'
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
    python_requires=">=3.7"
)
