# Makefile

.PHONY: regen
regen:
	python _src/update.py cloud-computing/
	python _src/update.py database-systems/
	python _src/update.py mlsys/
	python _src/update.py programming-languages/
	python _src/update.py storage-systems/

.PHONY: format
format:
	black _src/update.py