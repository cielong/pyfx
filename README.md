# pyfx
[![Build Status](https://travis-ci.org/cielong/pyfx.svg?branch=master)](https://travis-ci.org/github/cielong/pyfx)
[![Documentation Status](https://readthedocs.org/projects/python-fx/badge/?version=latest)](https://python-fx.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/python-fx.svg)](https://badge.fury.io/py/python-fx)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/cielong/pyfx)
![GitHub](https://img.shields.io/github/license/cielong/pyfx)  

Inspired by [fx](https://github.com/antonmedv/fx), a python implementation of JSON Viewer TUI.

## Installation
### Use pip
Before using pip, please check your Python version, pyfx requires >= 3.8.
```bash
pip install python-fx
```
### Build From Source
Clone the this [repo](https://github.com/cielong/pyfx.git), change directory into the project and run
```bash
python setup.py install
```

## Usage
### CLI
*pyfx* comes with a CLI, which you can use to directly open a JSON file.  
* You can use it to open a JSON file
  ```bash
   pyfx JSON_FILE
  ```
* You can also use it to open JSON data from a pipe
  ```bash
   cat JSON_FILE | pyfx
  ```
### Import as Module
#### Import *pyfx* Simple TUI
You can directly integrate *pyfx*'s TUI into your own project.   
One would expect this to be the last step of your CLI application. The method `Controller#run_with_data` contains a infinite loop [MainLoop](http://urwid.org/reference/main_loop.html#mainloop) to render image until exit (press `q`).
```python
from pyfx import Controller

...
# data is the what you want to render as TUI
# only supports dict, list and primitive variable
Controller().run_with_data(data)
```
#### Import *pyfx*'s Native JSON Library and Integrate with Your Own TUI
You can also import *pyfx* native JSON lib to integrate it into your own urwid TUI, e.g. [json_browser.py](https://github.com/cielong/pyfx/blob/master/src/pyfx/view/components/json_browser/json_browser.py).
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
*pyfx* can be configured using YAML, the config file is either passed directly through CLI option or automatically
loaded in predefined config folderq.

If *pyfx* is invoked without `-c / --config` option, it will search config file in with the following order:
1. ~/.config/pyfx/config.yml
2. PYTHON_DIR/site-packages/pyfx/config/config.yml

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


## Full Documentation
Please visit [Documentation](https://python-fx.readthedocs.io/en/latest/)

## License
Please visit [LICENSE](https://github.com/cielong/pyfx/blob/master/LICENSE.txt)
