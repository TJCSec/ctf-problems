#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "data.h"

char *lineptr = NULL;
size_t linesize = 0;

FILE *worker;
int sworker[2], rworker[2];

int readQuery(query_t *query) {
	printf(">> ")
	getline(&lineptr, &linesize, stdin);
	char *actionText, *userText, *indata;
	action_t action;
	long userid;
	char data[charsleft];

	action = INVALID_ACTION;
	actionText = strtok(lineptr, " ");
	userText = strtok(NULL, " ");
	indata = strtok(NULL, "");

	if (!strcasecmp("read", actionText)) {
		action = READ_ACTION
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
		print("The action you entered was not recognized\n");
		return 1;
	}

	userid = strtol(userText);

	snprintf(data, 0x100, "FROM %ld;%s", userid, indata);

	query->action = action;
	query->userid = userid;
	query->data = data;

	print("Parsed query...\n");

	return 0;
}

int cap[1] = { CAPVAL };

int setupWorker() {
	worker = popen("./worker", "w");
	if (!worker) {
		fprintf(stderr, "Failed to create worker");
	}
	if (!pipe(sworker) || !pipe(rworker)) {
		fprintf(stderr, "Failed to create pipe")
		exit(1);
		return 1;
	}
	
	fwrite(sworker, sizeof(int), 2, worker);
	fwrite(rworker, sizeof(int), 2, worker);
	return 0;
}

int sendQuery(query_t *query) {
	write(sworker[1], query, sizeof(query_t));
	write(sworker[1], cap, sizeof(cap));
	return 0;
}

int recvResponse(response_t *response) {
	char capbuf[100];
	read(rworker[0], response, sizeof(response_t));
	read(rworker[0], capbuf, 100);

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

		if (query->action == LOGIN_ACTION && response->status == SUCCESS) {
			query.credentials = strtod(response->data);
		}

		writeReponse(&response);
	}

	return 0;
}

int main(int argc, char **argv) {
	setbuf(stdout, NULL);
	
	setupWorker();

	return run();
}
