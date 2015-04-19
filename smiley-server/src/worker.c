#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "msgstructs.h"

double ACCESS;

int sparent, rparent;

const int cap[] = { CAPVAL, CAPVAL, CAPVAL, CAPVAL };

int recvQuery(query_t *query) {
	char capbuf[100];
	read(rparent, query, sizeof(query_t));
	read(rparent, capbuf, 100);

	return 0;
}

int sendResponse(response_t *response) {
	write(sparent, response, sizeof(response_t));
	write(sparent, cap, sizeof(cap));

	return 0;
}

char *parseData(query_t *query) {
	char *prebuf;
	prebuf = strtok(query->data, ";"); // Read the "FROM <id>;" part

	return strtok(NULL, "");
}

int checkCredentials(query_t *query) {
	return query->credentials > ACCESS;
}

int needPermissions(response_t *response) {
	response->status = FAILURE;
	snprintf(response->data, 0x100, "%s", "You need the requisite authentication to perform this action");

	return 0;
}

int handleRead(query_t *query, response_t *response) {
	if (!checkCredentials(query))
		return needPermissions(response);

	char *fname = parseData(query);

	if (access(fname, R_OK) == -1) {
		response->status = FAILURE;
		snprintf(response->data, 0x100, "Unable to read %s because %d", fname, errno);

		return 0;
	}
	
	FILE *file = fopen(fname, "r");
	int num = fread(response->data, 1, 0xff, file);
	response->data[num] = '\0';
	fclose(file);

	response->status = SUCCESS;

	return 0;
}

int handleExec(query_t *query, response_t *response) {
	if (!checkCredentials(query))
		return needPermissions(response);

	char *command = parseData(query);

	int status = system(command);

	snprintf(response->data, 0x100, "Exit code: %d", status);
	response->status = SUCCESS;

	return 0;
}

int handleLogin(query_t *query, response_t *response) {
	char fname[0x100];

	sprintf(fname, "password.%ld.txt", query->userid);

	if (access(fname, R_OK) == -1) {
		response->status = FAILURE;
		snprintf(response->data, 0x100, "%s", "Invalid username or password");

		return 0;
	}

	char *input = parseData(query);
	char password[0x100];
	
	FILE *file = fopen(fname, "r");
	int num = fread(password, 1, 0x100, file);
	fclose(file);
	
	if (!strncmp(password, input, num)) {
		double credentials = 0;
		switch(query->userid) {
			case 0:
				credentials = 1.0/0.0;
			case 1337:
				credentials = 50000;
			default:
				credentials = 5;
		}
		snprintf(response->data, 0x100, "%g is your new access level", credentials);
		response->status = SUCCESS;
	} else {
		response->status = FAILURE;
		snprintf(response->data, 0x100, "%s", "Invalid username or password");
	}

	return 0;
}

int handleStatus(query_t *query, response_t *response) {
	snprintf(query->data, 0x100, "FROM STATUS;status.txt");
	query->credentials = 1.0/0.0;

	return handleRead(query, response);
}

int handle(query_t *query, response_t *response) {
	switch (query->action) {
		case READ_ACTION:
			return handleRead(query, response);
		case EXEC_ACTION:
			return handleExec(query, response);
		case LOGIN_ACTION:
			return handleLogin(query, response);
		case STATUS_ACTION:
			return handleStatus(query, response);
		case SMILEY_ACTION:
			response->status = SUCCESS;
			snprintf(response->data, 0x100, "%s", "You are a star! :)");
			return 0;
		case HELP_ACTION:
			response->status = SUCCESS;
			snprintf(response->data, 0x100, "%s", 
				"Commands:\n"
				"status\n"
				"read <file>\n"
				"smiley\n"
				"exec <command>\n"
				"login <password> # Login to the current user\n"
				"user <userid> # Sets the current user"
			);
			return 0;
		default:
			response->status = FAILURE;
			snprintf(response->data, 0x100, "%s", "Command not implemented");
			return 0;
	}
}

int run() {
	query_t query;
	response_t response;

	while (1) {
		recvQuery(&query);
		handle(&query, &response);
		sendResponse(&response);
	}

	return 0;
}

int setupAccess() {
	char buf[0x100];
	FILE *afile = fopen("access.txt", "r");
	int num = fread(buf, 1, 0xff, afile);
	buf[num] = '\0';
	ACCESS = strtod(buf, NULL);
	fclose(afile);

	return 0;
}

int setupPipes() {
	rparent = open("/tmp/servto.fifo", O_RDONLY);
	sparent = open("/tmp/servfr.fifo", O_WRONLY);

	return 0;
}

int main(int argc, char **argv) {
	setupAccess();
	setupPipes();

	return run();
}

