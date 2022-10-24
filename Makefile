.PHONY: clean
clean:
	rm -rf build dist *.egg-info

.PHONY: build
build:
	@echo "Freeze current dependency and generate requirements files"
	# ignore the header comments and -i lines generated from pipenv lock -r
	pipenv requirements | sed -n '/^\-i/,$$p' | tail -n +2 > requirements.txt
	pipenv requirements --dev | sed -n '/^\-i/,$$p' | tail -n +2 > dev-requirements.txt
	@echo "Use autopep8 to reformat the code."
	pipenv run autopep8 --recursive --in-place .

.PHONY: test
test: build
	pipenv run tox --recreate -v
	pipenv run coverage erase

.PHONY: package
package: clean test
	python3 -m build

.PHONY: install
install: clean test package
	python3 -m installer dist/*.whl

.PHONY: release
release: package
	twine upload --verbose dist/*
