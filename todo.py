#!/usr/bin/env python3


# todopy - a todo script written in python
# options:
#   a "text"    - add entry to todo-list
#   l           - list entries
#   r entry     - remove entry

import os
import sys


# first need to change working directory,
# change this to wherever you want to store your entries.

USER = "erik"
os.chdir("/home/" + USER + "/txt/todo")


# header message

def header():
    print("TODO-list:" + "\n")


# exit if no arguments are given

if len(sys.argv) < 2:
    print("usage: [a \"text\" | l | r entry]")
    sys.exit(2)

option = sys.argv[1]

if option == "a":

    if len(sys.argv) < 3:

        print("this option requires an additional argument")
        sys.exit(2)

    elif len(os.listdir()) == 0:

        current_entry = 1
        entry = open(str(current_entry), "w+")
        entry.write(sys.argv[2])
        entry.close()

    else:

        latest_entry = max(os.listdir())
        current_entry = str(int(latest_entry) + 1)
        entry = open(current_entry, "w+")
        entry.write(sys.argv[2])
        entry.close()

elif option == "l":

    header()

    # the list of entries displays in random order for whatever reason.
    # this is why there is a sorting step in the listing process.

    entrylist = os.listdir().sort()

    for entry in entrylist:
        f = open(entry, "r")
        print(entry + ": " + f.read())
        f.close()

elif option == "r":

    if len(sys.argv) < 3:
        print("this option requires an additional argument")
        sys.exit(2)

    elif len(os.listdir()) == 1:
        os.remove("1")

    else:
        for file in os.listdir():
            if int(file) > int(sys.argv[2]):
                entry_name = file
                new_name = int(file) - 1
                os.rename(entry_name, str(new_name))
