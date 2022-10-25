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
### Local Development
Clone the this [repo](https://github.com/cielong/pyfx.git), change directory into the project and run
```bash
pipenv install --dev
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
from pyfx import PyfxApp

data = [1]
# data is the JSON data to be rendered in the TUI
# only supports dict, list and primitive variable
PyfxApp(data=data).run()
```

#### Integrate with Your Own Urwid-based TUI
Integrate *Pyfx* native JSON widgets into your own urwid-based TUI.
```python
from pyfx.view.json_lib import JSONListBox, JSONListWalker

data = [1]

# 1. create JSONListBox from data
listbox = JSONListBox(JSONListWalker(data))

# 2. use listbox in your own TUI
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

| Name                          | Description                                            | Foreground Color   |
|-------------------------------|--------------------------------------------------------|--------------------|
| body                          | Pyfx body (JSON Browser)                               | terminal default   |
| foot                          | Pyfx footer (Query Bar and Help Bar)                   | gray               |
| focused                       | focused display                                        | gray               |
| **Auto Complete PopUp**                                                                                     |
| autocomplete_popup            | autocomplete popup                                     | black              |
| autocomplete_popup_focused    | focused display for autocomplete popup                 | white              |
| **JSON Browser**                                                                                            |
| json_key                      | object key                                             | blue               |
| json_string                   | *string* type value                                    | green              |
| json_integer                  | *integer* type value                                   | cyan               |
| json_numeric                  | *numeric* type value                                   | cyan               |
| json_bool                     | *boolean* type value                                   | yellow             |
| json_null                     | *null* type value                                      | red                |
| json_focused                  | focused display for JSON                               | gray               |

#### Key Bindings
Alternative key bindings, see [Key Bindings Configuration](https://python-fx.readthedocs.io/en/latest/configuration/keymap.html).   

| Key              | Function                                          |
|------------------|---------------------------------------------------|
| q                | exit pyfx (except in Query Bar)                   |
| ?                | open help page (except in Query Bar)              |
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
| **Help PopUp**                                                       |
| up               | move cursor up one line                           |
| down             | move cursor down one line                         |
| esc              | close the help popup                              |

## Known Limitation
When open with very large JSON files, Pyfx will freeze on JSONPath query.  

The following statistics is tested at a MacBook Air (1.1GHz Quad-Core Intel Core i5
and 8GB RAM).

| File Size        | Functionality       | Usability                                    |
|------------------|---------------------|----------------------------------------------|
| 57MB             | Display JSON        | Fairly good                                  |
| ^^               | Query Autocomplete  | Latency <= 200ms                             |
| ^^               | Query JSONPath      | Roughly 1~2s latency                         |
| 570MB            | Display JSON        | Slow loading                                 |
| ^^               | Query Autocomplete  | Latency <= 200ms. Give up with large data    |
| ^^               | Query JSONPath      | UI may freeze depend on the search space     |

## License
The code is under [The MIT License](LICENSE.txt).

## Changelog
See the [changelog](CHANGELOG.md) for a history of notable changes to *Pyfx*.

## Contributors
* [Avery (@nullableVoidPtr)](https://github.com/nullableVoidPtr)

## How to Contribute
If you run into any issues, please let me know by creating a GitHub issue.
