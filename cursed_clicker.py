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
    save["store"] = {}
    save["store"]["clickers"] = 0
    with open("log.txt", "w") as f:
        f.write(str(type(save["store"])))
        for k,v in save["store"].items():
            f.write(f"{k},{v}\n")
def store(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0,0,"Welcome to the store!")
        stdscr.addstr(1,0, "Clickers add 0.5 to your cps (cookies per seconds)")
        stdscr.addstr(2,0, "Type 0 to exit the store.")
        line_at = 3
        line_started = 3
        for k,v in save["store"].items():
            stdscr.addstr(line_started, 0, f"{line_at - line_started + 1}:{k} {v}")
            line_at += 1
        stdscr.refresh()
        nput = stdscr.getkey()
        if nput == 1:
            save["store"]["clickers"] += 1
        if nput == 0:
            break

if not os.path.exists(save_file):
    # Create the save file
    initsave()
    save_to_json()
# Load our save file
with open(save_file, "r") as f:
    save = json.load(f)

def addcookie():
    save["cookies"] += save["store"]["clickers"] * 0.5
    save["cookies"] += 1


def main(stdscr):
    while True:
        try:
        # Print amount of cookies on top line
            stdscr.clear()
            stdscr.addstr(0,10,f"You have {save['cookies']} cookies.") 
            stdscr.addstr(1,10, "Type 1 for the shop")
            stdscr.refresh()
            nput = stdscr.getkey()
            # Check what to do

            # If \n, add cookie
            if nput == '\n':
                addcookie()
            # If 1, go to shop
            if nput == "1":
                store(stdscr)
        except KeyboardInterrupt:
            save_to_json()
            break
wrapper(main)

