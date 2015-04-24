all:
	docker build -t short-url src/
run:
	docker run -d -p 8095:5000 -t short-url
debug:
	docker run -i -p 8095:5000 -t short-url
shell:
	docker run -i -p 8095:5000 -t short-url /bin/bash
