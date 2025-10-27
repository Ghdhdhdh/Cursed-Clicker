from curses import wrapper
import json
import os

def save_to_json():
    with open(save_file, "w") as f:
        f.write(json.dumps(save))

# does the save.json exist?
save_file = "save.json"
save = {}
def initsave():
    save["cookies"] = 0
    save["cps"] = 1

if not os.path.exists(save_file):
    # Create the save file
    initsave()
    save_to_json()
# Load our save file
with open(save_file, "r") as f:
    save = json.load(f)

def addcookie():
    save["cookies"] += save["cps"]


def main(stdscr):
    while True:
        try:
        # Print amount of cookies on top line
            stdscr.clear()
            stdscr.addstr(0,10,f"You have {save['cookies']} cookies.") 
            stdscr.refresh()
            nput = stdscr.getkey()
            # Check what to do

            # If \n, add cookie
            if nput == '\n':
                addcookie()
        except KeyboardInterrupt:
            save_to_json()
            break
wrapper(main)

