.PHONY: clean
clean:
	rm -rf build dist *.egg-info

.PHONY: build
build:
	@echo "Use autopep8 to reformat the code."
	autopep8 --recursive --in-place .

.PHONY: test
test: build
	tox --recreate -v

.PHONY: install
install: clean test
	python setup.py install

.PHONY: package
package: clean test
	python3 setup.py sdist bdist_wheel

.PHONY: release
release: package
	twine upload --verbose dist/*
