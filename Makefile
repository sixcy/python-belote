MAIN=main

PYFILES=$(wildcard *.py)

all: $(MAIN).tok

%.tok: $(MAIN).py $(PYFILES)
	@mypy $< && touch $@

.PHONY:
run: $(MAIN).tok
	@./$(MAIN).py
