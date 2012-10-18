all: html pdf

pdf : MakeWayForPiggies.tex
	pdflatex MakeWayForPiggies.tex

MakeWayForPiggies.tex : context.json template.tex hashtag_hyphenation.json
	python render.py --context=context.json --template=template.tex --hyphenation=hashtag_hyphenation.json --output=MakeWayForPiggies.tex

html : context.json template.html 
	python render.py --context=context.json --template=template.html --output=index.html

context.json : MergedPosts.json sections.json preface.txt
	python generate_context.py --posts=MergedPosts.json --sections=sections.json --preface=preface.txt --output=context.json

clean:
	rm MakeWayForPiggies.tex
	rm MakeWayForPiggies.pdf
	rm index.html
	rm *.pyc
	rm *.aux
	rm *.log
	rm *.toc
