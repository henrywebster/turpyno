sync: requirements.txt
		. venv/bin/activate &&\
		pip install --quiet --requirement requirements.txt\

env:
	if ! [ -d venv ]; \
	then\
		python3 -m venv venv &&\
		touch requirements.txt;\
	fi

format: sync
	. venv/bin/activate &&\
	black turpyno/ tests/

clean:
	rm -rf venv

test: tests/ turpyno/
	. venv/bin/activate &&\
	mypy --disallow-untyped-defs turpyno/*.py tests/*.py &&\
	flake8 turpyno tests &&\
	pylint --extension-pkg-whitelist=pygame turpyno &&\
	safety check &&\
	bandit -r turpyno &&\
	python3 -m pytest -v


package: sync test dist/
	. venv/bin/activate &&\
	python3 setup.py sdist bdist_wheel

install: package
	. venv/bin/activate &&\
	twine upload --repository-url ${PYPI_REPO} dist/* -u . -p .

.PHONY: dist/ venv/ turpyno/ tests/ clean env sync
