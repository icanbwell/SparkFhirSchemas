LANG=en_US.utf-8

export LANG

BRANCH=$(shell git rev-parse --abbrev-ref HEAD)
VERSION=$(shell cat VERSION)
VENV_NAME=venv
GIT_HASH=${CIRCLE_SHA1}
SPARK_VER=3.0.1
HADOOP_VER=3.2
PACKAGES_FOLDER=venv/lib/python3.6/site-packages
SPF_BASE=${PACKAGES_FOLDER}

include spark_fhir_schemas/Makefile.spark
include spark_fhir_schemas/Makefile.docker
include spark_fhir_schemas/Makefile.python

.PHONY:devsetup
devsetup:venv
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt && \
    pip install --upgrade -r requirements-test.txt && \
    pre-commit install && \
    python setup.py install

.PHONY:checks
checks:venv
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade -r requirements.txt && \
    flake8 spark_fhir_schemas && \
    mypy spark_fhir_schemas --strict && \
    flake8 tests && \
    mypy tests --strict

.PHONY:update
update:
	. $(VENV_NAME)/bin/activate && \
	pip install --upgrade -r requirements.txt && \
	pip install --upgrade -r requirements-test.txt

.PHONY:build
build:venv
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt && \
    python setup.py install && \
    rm -r dist/ && \
    python3 setup.py sdist bdist_wheel

.PHONY:testpackage
testpackage:venv build
	. $(VENV_NAME)/bin/activate && \
	python3 -m twine upload -u __token__ --repository testpypi dist/*
# password can be set in TWINE_PASSWORD. https://twine.readthedocs.io/en/latest/

.PHONY:package
package:venv build
	. $(VENV_NAME)/bin/activate && \
	python3 -m twine upload -u __token__ --repository pypi dist/*
# password can be set in TWINE_PASSWORD. https://twine.readthedocs.io/en/latest/

.PHONY:tests
tests:
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade -r requirements.txt && \
	pip install --upgrade -r requirements-test.txt && \
	pytest tests

.PHONY:clean-pre-commit
clean-pre-commit:
	pre-commit clean

.PHONY:setup-pre-commit
setup-pre-commit:
	pre-commit install

.PHONY:run-pre-commit
run-pre-commit:
	pre-commit run --all-files

.PHONY:init
init: installspark up devsetup tests

.PHONY:schema
schema:
	. ${VENV_NAME}/bin/activate && \
	python3 spark_fhir_schemas/r4/generate_schema.py && \
	pre-commit run --all-files
	pre-commit run --all-files
# run twice to check that the formatting was fixed

.PHONY:setup_packages
setup_packages:
	pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt && \
    pip install --upgrade -r requirements-test.txt && \
    python setup.py install

.PHONY:continuous_integration
continuous_integration:
	pytest tests
