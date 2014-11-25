all:
	docker build -t simple-flask src/
run:
	docker run -d -p 8084:5000 -t simple-flask
debug:
	docker run -i -p 8084:5000 -t simple-flask
shell:
	docker run -i -p 8084:5000 -t simple-flask /bin/bash
