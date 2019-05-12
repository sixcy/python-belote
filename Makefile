MAIN=main

all: $(MAIN).tok

%.tok: %.py
	@mypy $< && touch $@

.PHONY:
run: $(MAIN).tok
	@./$(MAIN).py
