all: html pdf

pdf : MakeWayForPiggies.tex
	pdflatex MakeWayForPiggies.tex

MakeWayForPiggies.tex : context.json template.tex hashtag_hyphenation.json
	python render.py --context=context.json --template=template.tex --hyphenation=hashtag_hyphenation.json --output=MakeWayForPiggies.tex

html : context.json template.html 
	python render.py --context=context.json --template=template.html --output=index.html

context.json : MergedPosts.json sections.json preface.txt
	python generate_context.py --posts=MergedPosts.json --sections=sections.json --preface=preface.txt --version=`git log -1 --pretty="%h"` --output=context.json

clean:
	rm -f MakeWayForPiggies.tex
	rm -f MakeWayForPiggies.pdf
	rm -f index.html
	rm -f context.json
	rm -f *.pyc
	rm -f *.aux
	rm -f *.log
	rm -f *.toc
