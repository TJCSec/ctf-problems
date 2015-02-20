all:
	for subdir in *; do \
		if [ -e $$subdir/Makefile ]; then \
				echo Building $$subdir; \
				$(MAKE) -C $$subdir; \
		fi \
	done
		

run:
	for subdir in *; do \
		if [ -e $$subdir/Makefile ]; then \
				echo Running $$subdir; \
				$(MAKE) -C $$subdir run; \
		fi \
	done
		
stop:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)
