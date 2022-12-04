# Makefile

.PHONY: regen
regen:
	python _src/update.py cloud-computing/
	python _src/update.py database-systems/
	python _src/update.py mlsys/
	python _src/update.py programming-languages/
	python _src/update.py storage-systems/

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