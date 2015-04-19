#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>

#include "msgstructs.h"

#define RSTATUS_SKIP 1
#define RSTATUS_QUERY 0
#define RSTATUS_EXIT 2

char *lineptr = NULL;
size_t linesize = 0;

const int cap[] = { CAPVAL, CAPVAL, CAPVAL, CAPVAL };

FILE *worker;
char wpipe[100], rpipe[100];

int readQuery(query_t *query) {
	printf(">> ");
	ssize_t len = getline(&lineptr, &linesize, stdin);
	if (len < 1) {
		return RSTATUS_EXIT;
	} else if (len == 1) {
		return RSTATUS_SKIP;
	}
	lineptr[len-1] = '\0';
	char *actionText, *userText, *indata;
	action_t action;
	long userid;
	char data[0x100];

	action = INVALID_ACTION;
	actionText = strtok(lineptr, " ");
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
	} else if (!strcasecmp("help", actionText)) {
		action = HELP_ACTION;
	} else if (!strcasecmp("user", actionText)) {
		action = USER_ACTION;
	} else if (!strcasecmp("exit", actionText)) {
		return RSTATUS_EXIT;
	}

	if (action == INVALID_ACTION) {
		printf("The action you entered was not recognized. Try help.\n");
		return RSTATUS_SKIP;
	}

	if (action == USER_ACTION) {
		if (indata) {
			query->userid = strtol(indata, NULL, 0);
			printf("Set user to %ld\n", query->userid);
		} else {
			printf("No user id specified\n");
		}
		return RSTATUS_SKIP;
	}

	snprintf(data, 0x100, "FROM %ld;%s", query->userid, indata);

	query->action = action;
	memcpy(query->data, data, 0x100);

	return RSTATUS_QUERY;
}

int sendQuery(query_t *query) {
	FILE *sworker = fopen(wpipe, "w");
	fwrite(query, sizeof(query_t), 1, sworker);
	fwrite(cap, 1, sizeof(cap), sworker);
	fclose(sworker);
	return 0;
}

int recvResponse(response_t *response) {
	FILE *rworker = fopen(rpipe, "r");
	char capbuf[100];
	fread(response, sizeof(response_t), 1, rworker);
	fread(capbuf, 1, 100, rworker);
	fclose(rworker);

	return 0;
}

int writeResponse(response_t *response) {
	if (response->status == SUCCESS) {
		printf("Your query succeeded.\n");
	} else {
		printf("Your query failed\n");
	}

	printf("Response:\n\n%s\n", response->data);

	return 0;
}

int run() {
	query_t query;
	response_t response;
	int rstatus;

	query.credentials = 0.0;
	query.userid = -1;

	while (1) {
		rstatus = readQuery(&query);
		if (rstatus == RSTATUS_EXIT) {
			printf("Exiting...");
			query.action = EXIT_ACTION;
			sendQuery(&query);
			return 0;
		} else if (rstatus == RSTATUS_SKIP) {
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

int setupWorker() {
	worker = popen("./worker", "w");
	setbuf(worker, NULL);
	if (!worker) {
		printf("Failed to create worker\n");
		exit(1);
		return 1;
	}

	srand(time(NULL) + clock());

	snprintf(wpipe, 100, "/tmp/servto.%d.fifo", rand());
	snprintf(rpipe, 100, "/tmp/servfr.%d.fifo", rand());

	mkfifo(wpipe, 0666);
	mkfifo(rpipe, 0666);

	fprintf(worker, "%s %s\n", wpipe, rpipe);
	fflush(worker);

	return 0;
}

int main(int argc, char **argv) {
	setbuf(stdout, NULL);
	
	setupWorker();

	int status = run();

	unlink(wpipe);
	unlink(rpipe);
	pclose(worker);

	return status;
}
