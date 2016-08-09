# EscapeTheTrolls
/r/dailyprogrammer Weekly #25 challenge Escape The Trolls
<https://www.reddit.com/r/dailyprogrammer/comments/4vrb8n/weekly_25_escape_the_trolls/>

EscapeTheTrolls is a command line based game where you play as an explorer who must escape the maze while avoiding roaming trolls.

### How to run
Execute the command `python main.py`

### How to play
* Explorer `< ^ > v`
* Troll `O`
* Exit `X`
* Wall `#`

Use the keyboard arrow keys to control the explorer. Each movement (changing direction or moving one space) uses a turn and will trigger the trolls to move around.

Press `q` to quit at any time.

### How it works
The game is built with Python using the [curses](https://docs.python.org/3.5/howto/curses.html) library for screen painting and keyboard handling.

Note: If running in Windows, you must install the Windows binaries for curses, available here.
<https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses>

`pip install curses-2.2-cp35-none-win32.whl`
