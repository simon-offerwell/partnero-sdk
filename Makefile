# Define which targets are not files
.PHONY: all install test

# Define default make command
all: install test

# Install dependencies
install:
	poetry install

# Run tests with pytest
test:
	poetry run pytest
