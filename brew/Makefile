all:
	docker build -t brew src/
run:
	docker run -d -p 8088:8080 -t brew
debug:
	docker run -i -p 8088:8080 -t brew
shell:
	docker run -i -p 8088:8080 -t brew /bin/bash
