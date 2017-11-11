
import util

class State():

	def __init__(self, prevBoard, moveColumn, moveSymbol):
		
		if prevBoard != None:
			self.board = util.copyBoard(prevBoard)	# copy board of previous state
			self.lastMoveSym = moveSymbol			# record symbol that led to this state

			# find lowest open position in column
			row = 0
			for i in range(0, len(self.board)):
				row = i
				if self.board[row][moveColumn] != None:
					row -= 1
					break

			if row < 0:
				print "ILLEGAL MOVE IN STATE CONSTRUCTOR"

			self.board[row][moveColumn] = moveSymbol	# update board to reflect move
			self.moveFromPrev = (row, moveColumn)		# set last move position

	# display state to console
	def logState(self):
		for i in range(0, len(self.board[0])):
			print i,
		print ""
		for row in self.board:
			for col in row:
				if col == util.Symbol.X:
					print "X",
				elif col == util.Symbol.O:
					print "O",
				else:
					print "_",
			print ""

	# populate the initial state based on row / col dimensions of game
	def constructInitState(self, rowDimensions, colDimensions):
		self.board = []
		self.lastMoveSym = None
		self.moveFromPrev = None

		for r in range(0, rowDimensions):
			self.board.append([])
			for c in range(0, colDimensions):
				self.board[r].append(None)

	# check if state is win relative to last move symbol
	def isWin(self):
		pass

	# check if state is tie (if all positions filled)
	def isTie(self):
		pass

	# get list of successors of a state, using moves of a given symbol only
	def getSuccessors(self, currentSymbol):
		pass