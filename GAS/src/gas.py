#!/usr/bin/env python2

import json
import sys
import hashlib


admin_file = "admin.json"
admins = None
grades_file = "grades.json"
grades = None

loggedin = False
isadmin = False

def write_grades():
    json.dump(grades, open(grades_file, 'w'))

def load_grades():
    return json.load(open(grades_file, 'r'))

def load_admins():
    return json.load(open(admin_file, 'r'))

def print_help():
    print "-- GAS Help --"
    print "                login <key>: log in to the system using access key <key>"
    print "admin <username> <password>: log in as administrator <username> using password <password>"
    print "                       help: print this help"
    print ""
    sys.stdout.flush()

def print_loggedin_help():
    print "-- GAS Authenticated Help --"
    print "view: view your grades"
    print "help: print this help"
    sys.stdout.flush()

def length_error():
    print "Error: wrong number of arguments. Please try again."
    sys.stdout.flush()

def process_command(c):
    global loggedin, isadmin

    if c[0] == "help":
        print_help()

    elif c[0] == "login":
        if len(c) != 2:
            length_error()
            return

        for student in grades:
            if grades[student]["accesskey"] == c[1]:
                loggedin = student
                print "Login successful. Now logged in as \"%s\". For help run \"help\"." % grades[student]["name"]
                sys.stdout.flush()
                return
        
        print "Invalid access key. Please try again."
        sys.stdout.flush()

    elif c[0] == "admin":
        if len(c) != 3:
            length_error()
            return

        for admin in admins:
            if admins[admin]["username"] == c[1] and admins[admin]["password"] == c[2]:
                loggedin = admin
                isadmin = True
                print "Admin login successful. Now logged in as \"%s\". For help run \"help\"." % admins[admin]["username"]
                sys.stdout.flush()
                return

        print "Invalid username and/or password. Please try again."
        sys.stdout.flush()

    else:
        print "Invalid command."
        sys.stdout.flush()

def process_loggedin_command(c):
    if c[0] == "help":
        print_loggedin_help()

    elif c[0] == "view":
        print "Your grades are:"
        for grade in grades[loggedin]["grades"]:
            print "%s: %s" % (grade, grades[loggedin]["grades"][grade])
        sys.stdout.flush()

    else:
        print "Invalid command."
        sys.stdout.flush()

def process_admin_command(c):
    global grades

    if c[0] == "help":
        print_admin_help()

    elif c[0] == "add":
        sys.stdout.write("Name of student to add: ")
        sys.stdout.flush()
        name = sys.stdin.readline().strip()

        print "Enter student's grades in the format \"Chemistry A\", with the class first then the letter grade. End with an empty line."
        sys.stdout.flush()
        usergrades = {}
        g = True
        while g:
            g = sys.stdin.readline().strip().split()
            usergrades[' '.join(g[:-1])] = g[-1]

        grades[max(grades.keys())+1] = {"name": name, "accesskey": hashlib.md5(name).hexdigest(), "grades": usergrades}

        write_grades()

    else:
        print "Invalid command. More coming in GAS V2.0."
        sys.stdout.flush()


def main():
    global grades, admins

    grades = load_grades()
    admins = load_admins()

    print "==== OFFICIAL GRADE ACCESS SYSTEM V1.0 ===="
    print "ACCESS TO THIS SYSTEM IS FOR AUTHORIZED USERS ONLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    sys.stdout.flush()

    print_help()

    while True:    
        sys.stdout.write('command: ')
        sys.stdout.flush()

        command = sys.stdin.readline()
        if not command:
            break # EOF

        command = command.strip().split()
        if not command:
            continue # Empty line

        if not loggedin:
            process_command(command)
        elif isadmin:
            process_admin_command(command)
        else:
            process_loggedin_command(command)

if __name__ == '__main__':
    main()
