clean-docs:
	jupyter-book clean docs

build-docs:
	jupyter-book build docs
	cp CNAME docs/_build/html/CNAME
	cp docs/.nojekyll docs/_build/html/.nojekyll

all-docs:
	make clean-docs;
	make build-docs
