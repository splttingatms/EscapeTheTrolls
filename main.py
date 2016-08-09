from escapeTheTrollsGame import EscapeTheTrollsGame
from curses import wrapper

def main(stdscr):
	game = EscapeTheTrollsGame(stdscr)
	game.run()

wrapper(main)