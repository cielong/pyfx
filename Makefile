.PHONY: clean
clean:
	rm -rf build dist *.egg-info

.PHONY: build
build:
	@echo "Freeze current dependency and generate requirements files"
	# ignore the header comments and -i lines generated from pipenv lock -r
	pipenv lock -r | sed -n '/^\-i/,$$p' | tail -n +2 > requirements.txt
	pipenv lock -r --dev | sed -n '/^\-i/,$$p' | tail -n +2 > dev-requirements.txt
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
