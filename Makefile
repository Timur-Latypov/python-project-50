install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff

make lint:
	poetry run flake8 gendiff

make test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

build: check
	poetry build