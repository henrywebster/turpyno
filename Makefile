sync: requirements.txt venv/
	python3 -m venv venv &&\
	. venv/bin/activate &&\
	pip install -r requirements.txt

format: sync
	. venv/bin/activate &&\
	black turpyno/ tests/

clean:
	rm -rf venv

test: sync tests/ turpyno/
	. venv/bin/activate &&\
	mypy --disallow-untyped-defs turpyno/*.py tests/*.py &&\
	flake8 turpyno tests &&\
	python3 -m pytest -v

package: test dist/
	. venv/bin/activate &&\
	python3 setup.py sdist bdist_wheel

install: package
	. venv/bin/activate &&\
	twine upload --repository-url ${PYPI_REPO} dist/* -u . -p .

.PHONY: dist/ venv/ turpyno/ tests/ requirements.txt clean
