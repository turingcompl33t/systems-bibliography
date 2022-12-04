# Makefile

default: all

# Run all scripts
.PHONY: all
all:
	python _src/all.py . --verbose

# Sort imports
.PHONY: sort
sort:
	isort -e --line-length 80 _src/*.py

# Format source
.PHONY: format
format:
	black _src/*.py

.PHONY: qa
qa: sort format