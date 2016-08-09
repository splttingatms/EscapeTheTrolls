from direction import Direction

def isMoveCommand(userInput):
	return userInput == "KEY_UP" or userInput == "KEY_DOWN" or userInput == "KEY_LEFT" or userInput == "KEY_RIGHT"

class Movable(object):
	def __init__(self, game):
		self.game = game
		self.dungeon = game.dungeon
		self.direction = Direction.SOUTH

		randomEmptyCell = self.game.dungeon.getRandomEmptyCell()
		self.positionX = randomEmptyCell[0]
		self.positionY = randomEmptyCell[1]

class Troll(Movable):
	def __init__(self, game):
		Movable.__init__(self, game)

	def draw(self):
		self.game.stdscr.addstr(self.positionY, self.positionX, "O")

	def update(self, userInput):
		if not isMoveCommand(userInput):
			return
		self.direction = self.game.random.randint(0, 3)
		self.updatePosition()

	def updatePosition(self):
		if self.direction == Direction.NORTH:
			if self.dungeon.isInBounds(self.positionX, self.positionY - 1) and not self.dungeon.isWall(self.positionX, self.positionY - 1):
				self.positionY = self.positionY - 1
		elif self.direction == Direction.EAST:
			if self.dungeon.isInBounds(self.positionX + 1, self.positionY) and not self.dungeon.isWall(self.positionX + 1, self.positionY):
				self.positionX = self.positionX + 1
		elif self.direction == Direction.SOUTH:
			if self.dungeon.isInBounds(self.positionX, self.positionY + 1) and not self.dungeon.isWall(self.positionX, self.positionY + 1):
				self.positionY = self.positionY + 1
		else:
			if self.dungeon.isInBounds(self.positionX - 1, self.positionY) and not self.dungeon.isWall(self.positionX - 1, self.positionY):
				self.positionX = self.positionX - 1

class Explorer(Movable):
	def __init__(self, game):
		Movable.__init__(self, game)

	def draw(self):
		character = "V"
		if self.direction == Direction.NORTH:
			character = "^"
		elif self.direction == Direction.EAST:
			character = ">"
		elif self.direction == Direction.SOUTH:
			character = "V"
		else:
			character = "<"
		self.game.stdscr.addstr(self.positionY, self.positionX, character)

	def update(self, userInput):
		direction = None
		if userInput == "KEY_UP":
			direction = Direction.NORTH
		elif userInput == "KEY_RIGHT":
			direction = Direction.EAST
		elif userInput == "KEY_DOWN":
			direction = Direction.SOUTH
		elif userInput == "KEY_LEFT":
			direction = Direction.WEST

		# update position first so that changing direction spends 1 turn
		self.updatePosition(direction)
		self.updateDirection(direction)

	def updateDirection(self, direction):
		if direction is not None:
			self.direction = direction

	def updatePosition(self, direction):
		if self.direction != direction:
			return

		if direction == Direction.NORTH:
			if self.dungeon.isWall(self.positionX, self.positionY - 1) and self.dungeon.canPush(self.positionX, self.positionY - 1, self.direction):
				self.dungeon.push(self.positionX, self.positionY - 1, self.direction)
			if not self.dungeon.isWall(self.positionX, self.positionY - 1):
				self.positionY = self.positionY - 1
		elif direction == Direction.EAST:
			if self.dungeon.isWall(self.positionX + 1, self.positionY) and self.dungeon.canPush(self.positionX + 1, self.positionY, self.direction):
				self.dungeon.push(self.positionX + 1, self.positionY, self.direction)
			if not self.dungeon.isWall(self.positionX + 1, self.positionY):
				self.positionX = self.positionX + 1
		elif direction == Direction.SOUTH:
			if self.dungeon.isWall(self.positionX, self.positionY + 1) and self.dungeon.canPush(self.positionX, self.positionY + 1, self.direction):
				self.dungeon.push(self.positionX, self.positionY + 1, self.direction)
			if not self.dungeon.isWall(self.positionX, self.positionY + 1):
				self.positionY = self.positionY + 1
		else:
			if self.dungeon.isWall(self.positionX - 1, self.positionY) and self.dungeon.canPush(self.positionX - 1, self.positionY, self.direction):
				self.dungeon.push(self.positionX - 1, self.positionY, self.direction)
			if not self.dungeon.isWall(self.positionX - 1, self.positionY):
				self.positionX = self.positionX - 1

		if self.dungeon.isExit(self.positionX, self.positionY):
			self.game.win()

		for gameObject in self.game.gameObjects:
			if isinstance(gameObject, Troll) and gameObject.positionX == self.positionX and gameObject.positionY == self.positionY:
				self.game.lose()
