all: html pdf

pdf: PreggoPosts.tex
	pdflatex PreggoPosts.tex

html: format.py
	python format.py
