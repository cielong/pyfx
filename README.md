# Pyfx
[![Build Status](https://travis-ci.org/cielong/pyfx.svg?branch=master)](https://travis-ci.org/github/cielong/pyfx)
[![Documentation Status](https://readthedocs.org/projects/python-fx/badge/?version=latest)](https://python-fx.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/python-fx.svg)](https://badge.fury.io/py/python-fx)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/cielong/pyfx)
![GitHub](https://img.shields.io/github/license/cielong/pyfx)  

A python-native JSON Viewer TUI, inspired by [fx](https://github.com/antonmedv/fx).  
*pyfx* supports:
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

## Usage
You can use *pyfx* in two ways:
* A standalone CLI tool
* A python module which can be integrated in any python CLI application

Check the [Documentation](https://python-fx.readthedocs.io/en/latest/) for details.
### CLI
*pyfx* comes with a CLI
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
#### Directly Attach *pyfx* Simple TUI
Directly integrate *pyfx*'s TUI into your own project.  
Normally, one would expect this to be the last step of your CLI application. The method `Controller#run_with_data` contains a infinite loop [MainLoop](http://urwid.org/reference/main_loop.html#mainloop) to render image until exit.
```python
from pyfx import Controller

...
# data is the what you want to render as TUI
# only supports dict, list and primitive variable
Controller().run_with_data(data)
```
#### Integrate with Your Own urwid-based TUI
You can also import *pyfx* native JSON lib to integrate it into your own urwid TUI, e.g. [json_browser.py](src/pyfx/view/components/json_browser/json_browser.py).
```python
from pyfx.view.json_lib import JSONListBox, JSONListWalker, NodeFactory

...
# create top node from the data (only supports dict, list and primitive variable)
top_node = NodeFactory.create_node("", data, display_key=False)
# create JSONListBox from top node, a urwid ListBox compatible widget (http://urwid.org/reference/widget.html#listbox)
listbox = JSONListBox(JSONListWalker(top_node))
# use listbox in your own TUI 
...
```
## Configuration
*pyfx* is configured using YAML, the config file is either passed directly through CLI option (`-c` | `--config`) or automatically
loaded in predefined config folder.

If no `-c / --config` option, it will try to search config file with the following order:
1. ~/.config/pyfx/config.yml

As the last effort, it will resolve the package default [config](src/pyfx/config/config.yml). Please also refer to
this config as an example when creating your own config file.

### Predefined Key Mappings
Key mapping is configured with the following configuration schema
```
keymap:
  mode: string, accepted_options = ["basic" (The default) | "emacs" | "vim"]
```
#### Basic Mode
| Key              | Function                                          |
|------------------|---------------------------------------------------|
| q                | exit pyfx (except in Query Bar)                   |
| **JSON Browser**                                                     |
| up               | move cursor up one line                           |
| down             | move cursor down one line                         |
| enter            | toggle expansion                                  |
| .                | enter query window (used to input JSONPath query) |
| **Query Bar**                                                        |
| enter            | apply JSONPath query and switch to JSON Browser   |
| esc              | cancel query and restore to state before query    |

#### Emacs Mode
To enable, add the following configuration in your config file:
```yaml
keymap:
  mode: "emacs"
```
##### Mapped Keys
| Key              | Function                                          |
|------------------|---------------------------------------------------|
| q                | exit pyfx (except in Query Bar)                   |
| **JSON Browser**                                                     |
| up / ctrl p      | move cursor up one line                           |
| down / ctrl n    | move cursor down one line                         |
| enter            | toggle expansion                                  |
| . / meta x       | enter query window (used to input JSONPath query) |
| **Query Bar**                                                        |
| enter            | apply JSONPath query and switch to JSON Browser   |
| ctrl g           | cancel query and restore to state before query    |

#### Vim Mode
To enable, add the following configuration in your config file:
```yaml
keymap:
  mode: "vim"
```
##### Mapped Keys
| Key              | Function                                          |
|------------------|---------------------------------------------------|
| q                | exit pyfx (except in Query Bar)                   |
| **JSON Browser**                                                     |
| up / k           | move cursor up one line                           |
| down / j         | move cursor down one line                         |
| enter            | toggle expansion                                  |
| . / :            | enter query window (used to input JSONPath query) |
| **Query Bar**                                                        |
| enter            | apply JSONPath query and switch to JSON Browser   |
| esc              | cancel query and restore to state before query    |

## License
The code is under [The MIT License](LICENSE.txt).

## Changelog
See the [changelog](CHANGELOG.md) for a history of notable changes to *pyfx*.

## How to Contribute
If you run into any issues, please let me know by creating a GitHub issue.
