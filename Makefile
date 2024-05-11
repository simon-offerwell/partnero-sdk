# Define which targets are not files
.PHONY: all install lint test build

# Define default make command
all: install lint test build

# Install dependencies
install:
	poetry install

# Build package
build:
	poetry build

# Run tests with pytest
test:
	poetry run pytest

# Run linter with ruff
lint:
	poetry run ruff check partnero