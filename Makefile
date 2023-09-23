# Variables
PYTHON = python3
PIP = pip3

# Install project dependencies
install:
    $(PIP) install -r requirements.txt

# Clean the project directory
clean:
    rm -rf build

# Build the project
build: clean
    # Add build commands here, if necessary

# Run the project
run:
    $(PYTHON) app.py

# Test the project
test:
    $(PYTHON) -m pytest tests

# Generate code coverage report
coverage:
    $(PYTHON) -m pytest --cov=app tests

# Run linters
lint:
    pylint app.py

# Run all checks
check: lint test coverage

# Help - display available commands
help:
    @echo "Available commands:"
    @echo "  install  - Install project dependencies"
    @echo "  clean    - Clean the project directory"
    @echo "  build    - Build the project"
    @echo "  run      - Run the project"
    @echo "  test     - Run tests"
    @echo "  coverage - Generate code coverage report"
    @echo "  lint     - Run linters"
    @echo "  check    - Run all checks"
    @echo "  help     - Display available commands"

# Default command - display help
.DEFAULT_GOAL := help
