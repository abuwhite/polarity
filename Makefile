install:
	poetry install

clean:
	 rm -rf /home/notabu/python-project-lvl2/dist/*

build: clean
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

gendiff:
	poetry run gendiff