all : html pdf
html : build/index.html static_files
pdf : build/MakeWayForPiggies.pdf

.PHONY : all html pdf static_files

build/MakeWayForPiggies.pdf : MakeWayForPiggies.tex static_files
	pdflatex -output-directory=build MakeWayForPiggies.tex
	pdflatex -output-directory=build MakeWayForPiggies.tex

MakeWayForPiggies.tex : context.json template.tex hashtag_hyphenation.json build
	python render.py --context=context.json --template=template.tex --hyphenation=hashtag_hyphenation.json --output=MakeWayForPiggies.tex

static_files : static_files/*
	cp -r $? build/

build/index.html : context.json template.html build
	python render.py --context=context.json --template=template.html --output=build/index.html

build :
	mkdir -p build

context.json : MergedPosts.json sections.json preface.txt
	python generate_context.py --posts=MergedPosts.json --sections=sections.json --preface=preface.txt --version=`git log -1 --pretty="%h"` --output=context.json

clean:
	rm -rf build/
	rm -f MakeWayForPiggies.tex
	rm -f MakeWayForPiggies.pdf
	rm -f index.html
	rm -f context.json
	rm -f *.pyc
	rm -f *.aux
	rm -f *.log
	rm -f *.toc
