# configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import pathlib
import sys
sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------

project = 'Pyfx'
copyright = '2020, Yutian Wu'
author = 'Yutian Wu'

# The full version, including alpha/beta/rc tags
# Get the version from the __version__.py file
root = pathlib.Path(__file__).parent.parent.resolve()


def get_version(version_file):
    about = {}
    with open(version_file, 'r') as fp:
        exec(fp.read(), about)
    return about["__version__"]


# get the version from the __version__.py file
release = get_version(root / 'src' / 'pyfx' / '__version__.py')

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_click'
]
# Turn on sphinx.ext.autosummary
autodoc_inherit_docstrings = False
autosummary_generate = True

# Napoleon configs
napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '_templates', 'Thumbs.db', '.DS_Store']

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    "_static"
]

# A list of CSS files. The entry must be a filename string or a tuple containing
# the filename string and the attributes dictionary. The filename must be
# relative to the html_static_path, or a full URI with scheme like
# http://example.org/style.css.
# The attributes is used for attributes of <link> tag. It defaults to an
# empty list.
html_css_files = [
    'css/color.css'
]

# A string of reStructuredText that will be included at the beginning of every
# source file that is read. This is a possible place to add substitutions that
# should be available in every file (another being rst_epilog). An example:
rst_prolog = """
.. include:: <s5defs.txt>

"""
