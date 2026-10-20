.PHONY: all clean install_deps test build

all: clean install_deps test build

clean:
	pyb clean

install_deps:
	pip install -r requirements.txt

test:
	pyb run_unit_tests

build:
	pyb package
