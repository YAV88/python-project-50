gendiff:
	poetry run gendiff


install: # Install programs
	poetry install


build: # build
	poetry build


publish: # Run publish
	poetry publish --dry-run


package-install: # package-install
	python3 -m pip install --user dist/*.whl


lint: # Linter
	poetry run flake8 gendiff