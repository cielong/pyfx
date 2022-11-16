.PHONY: clean
clean:
	@echo "\nClean up directory.\n"
	rm -rf build dist *.egg-info

.PHONY: lint
lint: clean
	@echo "\nUse autopep8 to reformat the code.\n"
	autopep8 --recursive --in-place .

.PHONY: test
test: clean lint
	@echo "\nRun tests.\n"
	tox --recreate -v

.PHONY: build
build: clean lint test
	python3 -m build

.PHONY: install
install: clean lint test build
	pip install dist/*.whl

.PHONY: release
release: build
	twine upload --verbose dist/*
