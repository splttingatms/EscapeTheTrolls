from dungeon import Dungeon
from explorer import Explorer
from explorer import Troll
from random import Random
import curses

class EscapeTheTrollsGame():
	def __init__(self, stdscr):
		self.stdscr = stdscr
		self.random = Random()
		self.random.seed(1)

		self.gameObjects = []
		self.dungeon = Dungeon(self)
		self.player = Explorer(self)

		# player should update last to catch hits
		self.gameObjects = [
			self.dungeon,
			Troll(self),
			Troll(self),
			Troll(self),
			Troll(self),
			Troll(self),
			self.player]

		self.isGameOver = False
		self.isWinner = False

		curses.curs_set(False)
		self.stdscr.clear()

	def run(self):
		self.draw()
		while not self.isGameOver:
			self.update()
			self.draw()

		self.stdscr.addstr(9, 12, " -----------")
		self.stdscr.addstr(10, 12, "|           |")
		self.stdscr.addstr(11, 12, "| Game over |")
		self.stdscr.addstr(12, 12, "|           |")
		self.stdscr.addstr(13, 12, " -----------")
		if self.isWinner:
			self.stdscr.addstr(12, 14, "you win")
		else:
			self.stdscr.addstr(12, 14, "you lose")
		self.stdscr.getkey()

	def draw(self):
		for gameObject in self.gameObjects:
			gameObject.draw()
		self.stdscr.move(0, 0)

	def update(self):
		userInput = self.stdscr.getkey()
		if userInput == "q":
			self.lose()

		for gameObject in self.gameObjects:
			gameObject.update(userInput)

	def win(self):
		self.isGameOver = True
		self.isWinner = True

	def lose(self):
		self.isGameOver = True
		self.isWinner = False