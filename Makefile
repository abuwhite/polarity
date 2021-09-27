install:
	poetry install
	make build
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 polarity

test:
	poetry run pytest polarity tests/

test-cov:
	poetry run pytest --cov=polarity tests/ --cov-report xml

polarity:
	poetry run polarity