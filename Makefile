.PHONY: test
test:
	tox -v

.PHONY: install
install:
	python setup.py install

.PHONY: clean
clean:
	rm -rf build dist *.egg-info

.PHONY: package
package:
	python3 setup.py sdist bdist_wheel
