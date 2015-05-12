# A makefile for compiling simple latex files

SRC=$(wildcard *.tex)
PDF=$(SRC:.tex=.pdf)

all: $(PDF)
%.pdf: %.tex
	latexmk --pdf $<
	latexmk -c
	# write-good $< || true
	
clean: ; latexmk -C; rm -f *.bbl
