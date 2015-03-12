all:
	docker build -t webimage src/
run:
	docker run -d -p 8083:1337 -p 8090:8090 -t webimage
debug:
	docker run -i -p 8083:1337 -p 8090:8090 -t webimage
shell:
	docker run -i -p 8083:1337 -p 8090:8090 -t webimage /bin/bash
