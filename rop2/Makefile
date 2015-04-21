cdnify = ../utils/cdnify
serve = static/rop2.zip
dockname := rop2
progname := rop2

all: build

run:
	docker run -d -p 8093:1337 -t $(dockname)

nodocker:
	./localwrapper

build: mkdirs
	docker build -t $(dockname) dock/

compile: mkdirs
	gcc rop2.c -o dock/$(progname) -m32 -fno-stack-protector
	ln -s --force $(progname) dock/prog

copysrc: mkdirs
	zip $(serve) dock/rop2 rop1.c
	$(cdnify) $(serve)

mkdirs:
	mkdir -p grader dock static

