clean-docs:
	jupyter-book clean docs

build-docs:
	jupyter-book build docs

all-docs:
	make clean-docs;
	make build-docs
