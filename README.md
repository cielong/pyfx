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
### Import Module

### Key Mapping
| Key              | Function                                          |
|------------------|---------------------------------------------------|
| **Main Window**                                                      |
| enter            | toggle expansion                                  |
| up/ctrl p        | move cursor up one line                           |
| down/ctrl n      | move cursor down one line                         |
| **Query Window**                                                     |
| .                | enter query window (used to input JSONPath query) |
| enter            | apply JSONPath query and switch to Main Window    |
