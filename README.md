# Pyfx
[![Build Status](https://travis-ci.org/cielong/pyfx.svg?branch=master)](https://travis-ci.org/github/cielong/pyfx)
[![Documentation Status](https://readthedocs.org/projects/python-fx/badge/?version=latest)](https://python-fx.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/python-fx.svg)](https://badge.fury.io/py/python-fx)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/cielong/pyfx)
![GitHub](https://img.shields.io/github/license/cielong/pyfx)  

A python-native JSON Viewer TUI, inspired by [fx](https://github.com/antonmedv/fx).  
*Pyfx* supports:
* Read JSON files in terminal from several sources (file, pipe or clipboard).
* Query JSON files using JSONPath query.

![](docs/demo.gif)

## Table of Content

* [Prerequisite](#prerequisites)
* [Installation](#installation)
  * [PIP](#pip)
  * [Build from Source](#build-from-source)
* [Usage](#usage)
  * [CLI](#cli)
  * [Python Module](#python-module)
* [Configuration](#configuration)
* [License](#license)
* [Changelog](#changelog)
* [How to Contribute](#how-to-contribute)

## Prerequisites
* OS: MacOS / Linux
* python: >= 3.8
* pip

## Installation
### Pip
```bash
pip install python-fx
```
### Build from Source
Clone the this [repo](https://github.com/cielong/pyfx.git), change directory into the project and run
```bash
python setup.py install
```

## Quick Start
You can use *Pyfx* in two ways:
* A standalone CLI tool
* A python module which can be integrated in any python CLI application

For details, please check the hosted [documentation](https://python-fx.readthedocs.io/en/latest/).
### CLI
*Pyfx* comes with a CLI, use it
* To open a JSON file
  ```bash
   pyfx JSON_FILE
  ```
* To read JSON data from pipe
  ```bash
   cat JSON_FILE | pyfx
  ```
* To read JSON data from clipboard
  ```bash
   pyfx -x / --from-clipboard
  ```

### Python Module
#### Directly Attach *Pyfx* Simple TUI
Directly integrate *Pyfx*'s TUI into your own project.  
```python
from pyfx import Controller

# data is the JSON data to be rendered in the TUI
# only supports dict, list and primitive variable
Controller().run_with_data(data)
```
#### Integrate with Your Own Urwid-based TUI
Integrate *Pyfx* native JSON widgets into your own urwid-based TUI.
```python
from pyfx.view.json_lib import JSONListBox, JSONListWalker, NodeFactory

# 1. create top node from the data (only supports dict, list and primitive variable)
top_node = NodeFactory.create_node("", data, display_key=False)

# 2. create JSONListBox from top node
listbox = JSONListBox(JSONListWalker(top_node))

# 3. use listbox in your own TUI
```
## Configuration
*Pyfx* is configured using YAML. There are two ways to provide a configuration file: 
* Pass directly through CLI option (`-c` | `--config`).
* Create a config file in predefined folders and *Pyfx* will load it with best effort and
  use the default [config](src/pyfx/config/config.yml) if none is find.  
  The predefined folders are searched in following order, with the first exist one has high priority.  
  1. `~/.config/pyfx/config.yml`

For available configuration, see [configuration](https://python-fx.readthedocs.io/en/latest/Configuration/index.html).

## License
The code is under [The MIT License](LICENSE.txt).

## Changelog
See the [changelog](CHANGELOG.md) for a history of notable changes to *Pyfx*.

## How to Contribute
If you run into any issues, please let me know by creating a GitHub issue.
