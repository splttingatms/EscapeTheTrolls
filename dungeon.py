from direction import Direction
from explorer import Movable

class Dungeon():
	def __init__(self, game):
		self.game = game

		self.width = 37
		self.height = 23
		self.walls = [
			list("#####################################"),
			list("# #       #       #     #         # #"),
			list("# # ##### # ### ##### ### ### ### # #"),
			list("#       #   # #     #     # # #   # #"),
			list("##### # ##### ##### ### # # # ##### #"),
			list("#   # #       #     # # # # #     # #"),
			list("# # ####### # # ##### ### # ##### # #"),
			list("# #       # # #   #     #     #   # #"),
			list("# ####### ### ### # ### ##### # ### #"),
			list("#     #   # #   # #   #     # #     #"),
			list("# ### ### # ### # ##### # # # #######"),
			list("#   #   # # #   #   #   # # #   #   #"),
			list("####### # # # ##### # ### # ### ### #"),
			list("#     # #     #   # #   # #   #     #"),
			list("# ### # ##### ### # ### ### ####### #"),
			list("# #   #     #     #   # # #       # #"),
			list("# # ##### # ### ##### # # ####### # #"),
			list("# #     # # # # #     #       # #   #"),
			list("# ##### # # # ### ##### ##### # #####"),
			list("# #   # # #     #     # #   #       #"),
			list("# # ### ### ### ##### ### # ##### # #"),
			list("# #         #     #       #       # #"),
			list("#X###################################")]

	def draw(self):
		for row in self.walls:
			for cell in row:
				self.game.stdscr.addstr(cell)
			self.game.stdscr.addstr("\n")

	def update(self, userInput):
		return

	def isEmpty(self, x, y):
		for gameObject in self.game.gameObjects:
			if isinstance(gameObject, Movable) and gameObject.positionX == x and gameObject.positionY == y:
				return False
		return self.walls[y][x] == " "

	def isWall(self, x, y):
		return self.walls[y][x] == "#"

	def isExit(self, x, y):
		return self.walls[y][x] == "X"

	def isInBounds(self, x, y):
		return (x < self.width) and (y < self.height)

	def canPush(self, x, y, direction):
		if direction == Direction.NORTH:
			adjacent = (x, y - 1)
		elif direction == Direction.EAST:
			adjacent = (x + 1, y)
		elif direction == Direction.SOUTH:
			adjacent = (x, y + 1)
		else:
			adjacent = (x - 1, y)

		return self.isInBounds(adjacent[0], adjacent[1]) and self.isEmpty(adjacent[0], adjacent[1])

	def push(self, x, y, direction):
		self.walls[y][x] = " "

		if direction == Direction.NORTH:
			self.walls[y - 1][x] = "#"
		elif direction == Direction.EAST:
			self.walls[y][x + 1] = "#"
		elif direction == Direction.SOUTH:
			self.walls[y + 1][x] = "#"
		else:
			self.walls[y][x - 1] = "#"

	def getRandomEmptyCell(self):
		randomX = self.game.random.randint(0, self.width - 1)
		randomY = self.game.random.randint(0, self.height - 1)
		while not self.isEmpty(randomX, randomY):
			randomX = self.game.random.randint(0, self.width - 1)
			randomY = self.game.random.randint(0, self.height - 1)
		return (randomX, randomY)