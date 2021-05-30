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

test-tree:
	poetry run gendiff tests/fixtures/test_tree1.json tests/fixtures/test_tree2.json

test-flat:
	poetry run gendiff tests/fixtures/test_file1.json tests/fixtures/test_file2.json

gendiff:
	poetry run gendiff