# default target
all: preview

preview:
	jupyter-book build --all ../website
	open _build/html/index.html

publish:
	jupyter-book build --all ../website
	ghp-import -n -p -f _build/html
