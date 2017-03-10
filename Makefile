SOURCES := $(shell ls *.md)

all: $(SOURCES:%.md=%.html)

%.html: %.md
	python transform.py $^

clean:
	rm -r docs
