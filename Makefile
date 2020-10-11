.PHONY: clean
clean:
	rm -rf build dist *.egg-info

.PHONY: test
test:
	tox -v

.PHONY: install
install: test
	python setup.py install

.PHONY: package
package: test
	python3 setup.py sdist bdist_wheel
