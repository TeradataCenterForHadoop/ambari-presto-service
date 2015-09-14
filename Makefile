.PHONY: clean-pyc clean-build clean-test test clean

clean: clean-pyc clean-build clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm -fr build/
	rm -fr dist/

clean-test:
	rm -rf .tox/

test: clean-test
	tox -- -s tests

dist: clean-build clean-pyc
	python setup.py bdist
	ls -l dist