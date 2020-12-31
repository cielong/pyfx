# Pyfx
[![Build Status](https://travis-ci.com/cielong/pyfx.svg?branch=main)](https://travis-ci.com/github/cielong/pyfx)
[![Documentation Status](https://readthedocs.org/projects/python-fx/badge/?version=latest)](https://python-fx.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/python-fx.svg)](https://badge.fury.io/py/python-fx)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/cielong/pyfx)
![GitHub](https://img.shields.io/github/license/cielong/pyfx)
[![codecov](https://codecov.io/gh/cielong/pyfx/branch/main/graph/badge.svg?token=QRA9CDTRTJ)](https://codecov.io/gh/cielong/pyfx)  

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
* [Quick Start](#quick-start)
  * [CLI](#cli)
  * [Python Module](#python-module)
* [Configuration](#configuration)
  * [Default Configuration](#default-configuration)
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
Check [Key Bindings](#key-bindings) section for default key bindings.  
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
Check [Key Bindings](#key-bindings) section for default key bindings.
  
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

For available configuration, see [configuration](https://python-fx.readthedocs.io/en/latest/configuration/index.html).

### Default Configuration
#### Theme
Alternative key bindings, see [Theme Configuration](https://python-fx.readthedocs.io/en/latest/configuration/theme.html).   

| Name             | Description                                            | Foreground Color   |
|------------------|--------------------------------------------------------|--------------------|
| body             | Pyfx body (JSON Browser)                               | terminal default   |
| foot             | Pyfx footer (Query Bar and Help Bar)                   | gray               |
| focused          | focused display                                        | gray               |
| **Auto Complete PopUp**                                                                        |
| popup            | autocomplete popup                                     | black              |
| popup_focused    | focused display for autocomplete popup                 | white              |
| **JSON Browser**                                                                               |
| json_key         | object key                                             | blue               |
| json_string      | *string* type value                                    | green              |
| json_integer     | *integer* type value                                   | cyan               |
| json_numeric     | *numeric* type value                                   | cyan               |
| json_bool        | *boolean* type value                                   | yellow             |
| json_null        | *null* type value                                      | red                |
| json_focused     | focused display for JSON                               | gray               |

#### Key Bindings
Alternative key bindings, see [Key Bindings Configuration](https://python-fx.readthedocs.io/en/latest/configuration/keymap.html).   

| Key              | Function                                          |
|------------------|---------------------------------------------------|
| q                | exit pyfx (except in Query Bar)                   |
| **JSON Browser**                                                     |
| up               | move cursor up one line                           |
| down             | move cursor down one line                         |
| e                | expand all                                        |
| c                | collapse all                                      |
| enter            | toggle expansion                                  |
| .                | enter query window (used to input JSONPath query) |
| **Query Bar**                                                        |
| enter            | apply JSONPath query and switch to JSON Browser   |
| esc              | cancel query and restore to state before query    |
| **Autocomplete PopUp**                                               |
| up               | move cursor up one line                           |
| down             | move cursor down one line                         |
| enter            | select option and complete the query              |
| esc              | close pop up                                      |

## License
The code is under [The MIT License](LICENSE.txt).

## Changelog
See the [changelog](CHANGELOG.md) for a history of notable changes to *Pyfx*.

## How to Contribute
If you run into any issues, please let me know by creating a GitHub issue.
