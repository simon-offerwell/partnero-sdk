# Define which targets are not files
.PHONY: all install test lint

# Define default make command
all: install lint test

# Install dependencies
install:
	poetry install

# Run tests with pytest
test:
	poetry run pytest

# Run linter with ruff
lint:
	poetry run ruff check partnero