all:
	        docker build -t xinetd-test src/
run:
	        docker run -d -p 8071:1337 -t xinetd-test
debug:
			docker run -i -p 8071:1337 -t xinetd-test
shell:
			docker run -i -p 8071:1337 -t xinetd-test /bin/bash
