.PHONY: check clean description dist release test

check:
	python setup.py check

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

description:
	rst2html.py DESCRIPTION.rst > description.html

dist:
	python setup.py sdist --formats=gztar,zip bdist_wheel
	gpg --armor --detach-sign -u 5878672C -a dist/*.whl
	gpg --armor --detach-sign -u 5878672C -a dist/*.tar.gz
	gpg --armor --detach-sign -u 5878672C -a dist/*.zip

release:
	twine upload dist/*

test:
	py.test -v -m tryfirst --maxfail=1 tests
	py.test -v -m "not tryfirst" tests
