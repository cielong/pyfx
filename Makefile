.PHONY: clean
clean:
	@echo "Clean up directory.\n"
	rm -rf build dist *.egg-info
	@echo

.PHONY: lint
lint: clean
	@echo "Use autopep8 to reformat the code.\n"
	autopep8 --recursive --in-place .
	@echo

.PHONY: test
test: clean lint
	@echo "Run tests.\n"
	tox --recreate -v
	@echo

.PHONY: build
build: clean lint test
	@echo "Build the project.\n"
	python3 -m build
	@echo

.PHONY: install
install: clean lint test build
	@echo "Install the binary."
	pip install --force-reinstall dist/*.whl
	@echo

.PHONY: release
release: build
	twine upload --verbose dist/*
