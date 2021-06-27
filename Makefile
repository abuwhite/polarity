install:
	poetry install

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest gendiff tests/

test-cov:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

deploy: build package-install install test test-cov lint

git: deploy
	git add .
	git commit -m "project deploy test"
	git push

test-stylish:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

test-plain:
	poetry run gendiff --format plain tests/fixtures/file1.json tests/fixtures/file2.json

test-json:
	poetry run gendiff --format json tests/fixtures/file1.json tests/fixtures/file2.json

gendiff:
	poetry run gendiff