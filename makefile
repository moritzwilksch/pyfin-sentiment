install:
	pip install -e .
	pip install -r requirements.txt

test:
	pytest tests/