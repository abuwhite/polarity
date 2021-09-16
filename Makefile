install:
	poetry install
	make build
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 diffepy

test:
	poetry run pytest diffepy tests/

test-cov:
	poetry run pytest --cov=diffepy tests/ --cov-report xml

diffepy:
	poetry run diffepy