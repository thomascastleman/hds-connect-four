
import util

class State():

	def __init__(self, prevBoard, moveColumn, moveSymbol):
		self.board = util.copyBoard(prevBoard)	# copy board of previous state
		self.lastMoveSym = moveSymbol			# record symbol that led to this state

		# find lowest open position in column
		row = 0
		for i in range(1, len(self.board)):
			if board[row][moveColumn] == None:
				row = i
			else:
				break

		self.board[row][moveColumn] = moveSymbol	# update board to reflect move
		self.moveFromPrev = (row, moveColumn)		# set last move position


	def logState(self):
		pass

	def constructInitState(self, rowDimensions, colDimensions):
		pass

	def isWin(self):
		pass

	def isTie(self):
		pass

	def getSuccessors(self, currentSymbol):
		pass