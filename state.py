
import game
from util import *

class State(game.ConnectNGame):

	def __init__(self, prevBoard, moveColumn, moveSymbol):
		
		if prevBoard != None:
			self.board = copyBoard(prevBoard)	# copy board of previous state
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
				print "X" if col == Symbol.X else "O" if col == Symbol.O else "_",
			print ""

	# check if a given move can be legally made on this state
	def checkMoveLegality(self, col):
		return col in range(0, len(self.board[0])) and self.board[0][col] == None

	# check if state is win relative to last move symbol
	def isWin(self):
		pass

	# check if state is tie (if all positions filled)
	def isTie(self):
		for c in range(0, len(self.board[0])):
			if self.board[0][c] == None:
				return False
		return True

	# get list of successors of a state, using moves of a given symbol only
	def getSuccessors(self, currentSymbol):
		pass