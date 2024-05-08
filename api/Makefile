install:
	pip install -r requirements.txt

style:
	python -m black --line-length 79 .

lint:
	python -m flake8

test:
	LOG_LEVEL="INFO" PYTHONWARNINGS="ignore::DeprecationWarning" python -m unittest

create-migration:
	python -m src.scripts.create_migration --name $(name)

migrate:
	python -m src.views.migrations