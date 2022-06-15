install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/

format:
	black .
	isort .

publish:
	rm -rf dist
	python3 -m build
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository pypi dist/*