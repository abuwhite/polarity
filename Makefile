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

deeploy: build package-install install test test-cov lint

git: deeploy
	git add .
	git commit -m "fix"
	git push

test-stylish:
	poetry run gendiff tests/fixtures/stylish1.json tests/fixtures/stylish2.json

test-json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

test-yml:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

gendiff:
	poetry run gendiff