
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

	def constructInitState(self, rowDimensions, colDimensions):
		self.board = []
		self.lastMoveSym = None
		self.moveFromPrev = None

		for r in range(0, rowDimensions):
			self.board.append([])
			for c in range(0, colDimensions):
				self.board[r].append(None)

	def isWin(self):
		pass

	def isTie(self):
		pass

	def getSuccessors(self, currentSymbol):
		pass