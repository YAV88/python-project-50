test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check:
	selfcheck test lint


selfcheck:
	poetry check


install:
	poetry install


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 gendiff


.PHONY: install test lint selfcheck check build
