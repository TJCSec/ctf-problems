cdnify = ../utils/cdnify
serve = static/rop1.zip
dockname := rop1
progname := rop1

all: build

run:
	docker run -d -p 8094:1337 -t $(dockname)

nodocker:
	./localwrapper

build: mkdirs
	docker build -t $(dockname) dock/

compile: mkdirs
	gcc rop1.c -o dock/$(progname) -m32 -fno-stack-protector
	ln -s --force $(progname) dock/prog

copysrc: mkdirs
	zip $(serve) dock/rop1 rop1.c
	$(cdnify) $(serve)

mkdirs:
	mkdir -p grader dock static

