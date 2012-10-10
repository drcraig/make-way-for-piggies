all: html pdf

pdf: MakeWayForPiggies.tex
	pdflatex MakeWayForPiggies.tex

html: format.py
	python format.py
