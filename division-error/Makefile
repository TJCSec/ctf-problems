all:
	docker build -t division-error src/
run:
	docker run -d -p 8082:5000 -t division-error
debug:
	docker run -i -p 8082:5000 -t division-error
shell:
	docker run -i -p 8082:5000 -t division-error /bin/bash
