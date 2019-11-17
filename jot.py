'''
jot

shell tool for notes/reminders/stuff

by Kyle Guss


'jot write 353/final'
- 'jot' shell command sends parameters to our python script
- 'write' type shows intent to write
- '353/final' is our path

'jot remind 353/homework'
- 'remind' type will add to reminders list
- 'groceries' is our directory
- add twilio support for reminders daily in morning across all directories

'jot show 353' and 'jot show 353/final'
- 'show' type displays all notes/reminders from directory or specific note

'jot trash 353/' == 'jot trash 353' and 'jot trash 353/final'
- 'trash' type trashes specified file or directory
- 'trash' requires verify command

'jot trash last'
- trashes last file or directory


'''

import os
from pathlib import Path


jot_home = Path(Path.home(), "jot")


# show_notes() displays all notes in the supplied directory,
# or in the jot home if no directory is supplied
def show_notes(pathing=None):
    if pathing is None:
        show_notes(Path(jot_home))
    else:
        if pathing == jot_home:
            display_path = jot_home
        else:
            display_path = Path(jot_home, pathing)

        if display_path.is_dir():
            print("printing contents of directory {}".format(display_path))
            # TODO print contents of directory (i guess names off all text files)
        elif display_path.is_file():
            print("printing contents of file {}".format(display_path))
            # TODO print contents of file
        else:
            print("{} is not found".format(display_path))


# write new note at specified path or open existing note
# if no path to note supplied then we cant write
def write_note(pathing=None):
    if pathing is None:
        print("Need pathing to write note")
    else:
        if pathing == jot_home:
            print("can't write note in jot root")
        else:
            write_path = Path(jot_home, pathing)

        if write_path.is_file():
            print("adding to file {}".format(write_path))
            # TODO open existing file in text editor
        else:
            print("{} file was created and opened".format(write_path))
            # TODO create and open new file in text editor


def create_reminder(pathing=None):
    if pathing is None:
        print("Need pathing to write note")
    else:
        if pathing == jot_home:
            print("can't write note in jot root")
        else:
            remind_path = Path(jot_home, pathing)
        # TODO add reminder at 'remind_path' (need to figure out how im going to store this)


if __name__ == "__main__":
    show_notes()
