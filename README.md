# pyfx
[![Build Status](https://travis-ci.org/cielong/pyfx.svg?branch=master)](https://travis-ci.org/github/cielong/pyfx)  

Inspired by [fx](https://github.com/antonmedv/fx), a python implementation of JSON Viewer TUI.

## Installation
Clone the this [repo](https://github.com/cielong/pyfx.git), change directory into the project and run
```bash
python setup.py install
```

## Usage
### CLI
*pyfx* comes with a CLI, which you can use to directly open a JSON file.  
After installation, simply run
```bash
pyfx JSON_FILE
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
You can also import *pyfx* native JSON lib to integrate it into your own urwid TUI, e.g. [view_window.py](https://github.com/cielong/pyfx/blob/master/src/pyfx/view/components/view_window.py).
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

### Key Mapping
| Key              | Function                                          |
|------------------|---------------------------------------------------|
| **Main Window**                                                      |
| q                | exit pyfx                                         |
| .                | enter query window                                |
| **View Window**                                                      |
| enter            | toggle expansion                                  |
| up/ctrl p        | move cursor up one line                           |
| down/ctrl n      | move cursor down one line                         |
| **Query Window**                                                     |
| .                | enter query window (used to input JSONPath query) |
| enter            | apply JSONPath query and switch to View Window    |
| esc              | apply JSONPath query and exit Query Window        |
