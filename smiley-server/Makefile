all: build

run:
	docker run -d -p 8091:1337 -t smiley

nodocker:
	./wrapper

build:
	docker build -t smiley src/

copysrc:
	zip static/adminserver.zip src/worker.c src/adminserver.c src/msgstructs.h src/adminserver src/worker
	../utils/cdnify static/adminserver.zip


compile:
	gcc src/worker.c src/msgstructs.h -m32 -malign-double -o src/worker
	gcc src/adminserver.c src/msgstructs.h -m32 -o src/adminserver
