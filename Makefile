.PHONY: install quality style

check_dirs := src setup.py

clean:
	rm -rf docs/build

docs: clean
ifeq ($(origin smv), undefined)
	sphinx-build -M html docs/source docs/build
else
	sphinx-multiversion docs/source docs/build
endif

gh-pages:
	utils/gh-pages.sh

install:
	pip install -e ".[dev]"

quality:
	black --check $(check_dirs)
	isort --check-only $(check_dirs)
	flake8 $(check_dirs)

style:
	black $(check_dirs)
	isort $(check_dirs)
