package-install:
	uv tool install dist/python_project_49-0.1.0-py3-none-any.whl

brain-games:
	uv run brain-games

even:
	uv run brain-even

gcd:
	uv run brain-gcd

check: 
	test lint

build:
	uv build

lint:
	uv run ruff check brain_games

.PHONY: install test lint selfcheck check build