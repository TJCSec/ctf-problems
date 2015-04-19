#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>

#include "msgstructs.h"

char *lineptr = NULL;
size_t linesize = 0;

const int cap[] = { CAPVAL, CAPVAL, CAPVAL, CAPVAL };

FILE *worker;
int sworker, rworker;

int readQuery(query_t *query) {
	printf(">> ");
	ssize_t len = getline(&lineptr, &linesize, stdin);
	if (len <= 1) {
		printf("Exiting...\n");
		exit(1);
		return 1;
	}
	lineptr[len-1] = '\0';
	char *actionText, *userText, *indata;
	action_t action;
	long userid;
	char data[0x100];

	action = INVALID_ACTION;
	actionText = strtok(lineptr, " ");
	userText = strtok(NULL, " ");
	indata = strtok(NULL, "");

	if (!strcasecmp("read", actionText)) {
		action = READ_ACTION;
	} else if (!strcasecmp("exec", actionText)) {
		action = EXEC_ACTION;
	} else if (!strcasecmp("login", actionText)) {
		action = LOGIN_ACTION;
	} else if (!strcasecmp("status", actionText)) {
		action = STATUS_ACTION;
	} else if (!strcasecmp("smiley", actionText)) {
		action = SMILEY_ACTION;
	}

	if (action == INVALID_ACTION) {
		printf("The action you entered was not recognized\n");
		return 1;
	}

	userid = strtol(userText, NULL, 10);

	snprintf(data, 0x100, "FROM %ld;%s", userid, indata);

	query->action = action;
	query->userid = userid;
	memcpy(query->data, data, 0x100);

	printf("Parsed query...\n");

	return 0;
}

int setupWorker() {
	worker = popen("./worker", "w");
	if (!worker) {
		fprintf(stderr, "Failed to create worker");
	}

	mkfifo("/tmp/servto.fifo", 0666);
	mkfifo("/tmp/servfr.fifo", 0666);

	sworker = open("/tmp/servto.fifo", O_WRONLY);
	rworker = open("/tmp/servfr.fifo", O_RDONLY);
	return 0;
}

int sendQuery(query_t *query) {
	write(sworker, query, sizeof(query_t));
	write(sworker, cap, sizeof(cap));
	return 0;
}

int recvResponse(response_t *response) {
	char capbuf[100];
	read(rworker, response, sizeof(response_t));
	read(rworker, capbuf, 100);

	return 0;
}

int writeResponse(response_t *response) {
	if (response == SUCCESS) {
		printf("Your query succeeded\n");
	} else {
		printf("Your query failed\n");
	}

	printf("%s\n", response->data);

	return 0;
}

int run() {
	query_t query;
	response_t response;

	query.credentials = 0.0;

	while (1) {
		if (readQuery(&query)) {
			continue;
		}

		sendQuery(&query);
		recvResponse(&response);

		if (query.action == LOGIN_ACTION && response.status == SUCCESS) {
			query.credentials = strtod(response.data, NULL);
		}

		writeResponse(&response);
	}

	return 0;
}

int main(int argc, char **argv) {
	setbuf(stdout, NULL);
	
	setupWorker();

	return run();
}
