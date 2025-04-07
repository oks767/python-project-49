package-install:
	uv tool install dist/python_project_49-0.1.0-py3-none-any.whl

run:
	uv run brain-games

brain-games:
	uv run brain-games

check: test lint

build:
	uv build

lint:
	uv run ruff check brain_games

.PHONY: install test lint selfcheck check build