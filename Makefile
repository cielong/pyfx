.PHONY: clean
clean:
	rm -rf build dist *.egg-info

.PHONY: test
test:
	tox -v

.PHONY: install
install: clean test
	python setup.py install

.PHONY: package
package: clean test
	python3 setup.py sdist bdist_wheel

.PHONY: release
release: package
	twine upload --verbose dist/*
