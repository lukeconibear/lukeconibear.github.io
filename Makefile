clean-docs:
	jupyter-book clean docs

build-docs:
	jupyter-book build docs
	cp CNAME docs/_build/html/CNAME
	cp .nojekyll docs/_build/html/.nojekyll
	cp slides/* docs/_build/html/

all-docs:
	make clean-docs;
	make build-docs
