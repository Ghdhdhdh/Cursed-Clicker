from curses import wrapper
import curses
import json
import os
import math

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
    save["prices"] = {}
    save["prices"]["clickers"] = 5
    with open("log.txt", "w") as f:
        f.write(str(type(save["store"])))
        for k,v in save["store"].items():
            f.write(f"{k},{v}\n")
def store(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0,0,"Welcome to the store!")
        stdscr.addstr(1,0, f"Clickers add")
        stdscr.addstr(" 0.5", curses.A_BOLD)
        stdscr.addstr(" to your cps (cookies per seconds). Price is ")
        stdscr.addstr(f"{save['prices']['clickers']}", curses.A_BOLD)
        stdscr.addstr(2,0, "Type 0 to exit the store.")
        stdscr.addstr(3,0, f"Cookies: {save['cookies']}")
        line_at = 4
        line_started = 4
        for k,v in save["store"].items():
            stdscr.addstr(line_started, 0, f"{line_at - line_started + 1}: You have ")
            stdscr.addstr(f"{v} {k}", curses.A_BOLD)
            stdscr.addstr("(s)")
            if line_at - line_started + 1 == 1:
                stdscr.addstr(" Currently adds ")
                stdscr.addstr(f'{save["store"]["clickers"] * 0.5}', curses.A_BOLD)
                stdscr.addstr(" cps.")
            line_at += 1
        stdscr.refresh()
        nput = stdscr.getkey()
        if nput == str(1):
            if save["cookies"] >= save["prices"]["clickers"]:
                save["store"]["clickers"] += 1
                save["prices"]["clickers"] = math.floor(save["prices"]["clickers"] * 1.15) 
                save["cookies"] -= save["prices"]["clickers"]
        if nput == str(0):
            break

if not os.path.exists(save_file):
    # Create the save file
    initsave()
    save_to_json()
# Load our save file
with open(save_file, "r") as f:
    save = json.load(f)

def addcookie():
    save["cookies"] += calculate_cps()
def calculate_cps():
    cps = 0
    cps += save["store"]["clickers"] * 0.5
    cps += 1
    return cps

def main(stdscr):
    while True:
        try:
        # Print amount of cookies on top line
            stdscr.clear()
            stdscr.addstr(0,10,f"You have ") 
            stdscr.addstr(f"{save['cookies']}", curses.A_BOLD)
            stdscr.addstr(" cookies.")
            stdscr.addstr(1,10, "Type 1 for the shop")
            stdscr.addstr(2,10, f"Your current cps is ")
            stdscr.addstr(f"{calculate_cps()}", curses.A_BOLD)
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

