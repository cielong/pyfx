.PHONY: install
install:
	python setup.py install

.PHONY: test
test:
	tox -v
