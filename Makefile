# This file is part of Oasis
# https://github.com/znhv/polarity

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2021 Boris Zhenikhov

install:
	@poetry install
	@poetry build
	python3 -m pip install dist/*.whl --force-reinstall

clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

test:
	make lint
	make pytest
	make pytest-cov

lint:
	poetry run flake8 polarity

pytest:
	poetry run pytest polarity tests/

cov-check:
	poetry run pytest --cov=polarity tests/

pytest-cov:
	@poetry run pytest --cov=polarity --cov-config .coveragerc tests/ -sq --cov-report xml

build: test
	@poetry build

oasis:
	poetry run polarity