install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/

format:
	black .
	isort .