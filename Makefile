install:
	poetry install
	make build
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest gendiff tests/

test-cov:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

gendiff:
	poetry run gendiff