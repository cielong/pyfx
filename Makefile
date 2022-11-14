.PHONY: clean
clean:
	@echo "\nClean up directory.\n"
	rm -rf build dist *.egg-info
	pipenv clean
	pipenv run coverage erase

.PHONY: lock
lock: clean
	@echo "\nFreeze current dependency and generate requirements files.\n"
	# ignore the header comments and -i lines generated from pipenv lock -r
	pipenv requirements | sed -n '/^\-i/,$$p' | tail -n +2 > requirements.txt
	pipenv requirements --dev | sed -n '/^\-i/,$$p' | tail -n +2 > dev-requirements.txt

.PHONY: build
build: clean lock
	@echo "\nUse autopep8 to reformat the code.\n"
	pipenv run autopep8 --recursive --in-place .

.PHONY: test
test: clean build
	@echo "\nRun tests.\n"
	pipenv run tox --recreate -v

.PHONY: package
package: clean test
	python3 -m build

.PHONY: install
install: clean test package
	python3 -m installer dist/*.whl

.PHONY: release
release: package
	twine upload --verbose dist/*
