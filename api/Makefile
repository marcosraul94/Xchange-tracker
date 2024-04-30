install:
	pip install -r requirements.txt

style:
	python -m black .

style-check:
	python -m black --check .

lint-check:
	python -m flake8

test:
	python -m unittest

create-migration:
	python -m src.scripts.create_migration --name $(name)