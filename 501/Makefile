all:
	docker build -t 501 src/
run:
	docker run -d -p 8081:5000 -t 501
debug:
	docker run -i -p 8081:5000 -t 501
shell:
	docker run -i -p 8081:5000 -t 501 /bin/bash
