"""
`pyfx`'s models.

It loads data from various sources and applies and completes given JSONPath query
on the current loaded JSON data.

* query directly uses :py:mod:`jsonpath_ng`
* auto-completion is achieved by home-made :py:class:`pyfx.model.JSONPathAutoComplete`
"""
from .model import Model
