
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
		print ""
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
	def isWin(self, nToWin):
		row, col = self.moveFromPrev
		numRows, numCols = len(self.board), len(self.board[0])

		# get horizontal possible win
		rowSection = self.board[row]

		# get vertical possible win
		colSection = []
		for r in range(0, len(self.board)):
			colSection.append(self.board[r][col])

		# get northeast diagonal possible win
		r, c = row, col
		neSection = []

		while r + 1 < numRows and c - 1 >= 0:
			r += 1
			c -= 1
		neSection.append(self.board[r][c])
		while r - 1 >= 0 and c + 1 < numCols:
			r -= 1
			c += 1
			neSection.append(self.board[r][c])

		# get southeast diagonal possible win
		r, c = row, col
		seSection = []

		while r + 1 < numRows and c + 1 < numCols:
			r += 1
			c += 1
		seSection.append(self.board[r][c])
		while r - 1 >= 0 and c - 1 >= 0:
			r -= 1
			c -= 1
			seSection.append(self.board[r][c])

		rowWin = checkSectionForWin(rowSection, nToWin, self.lastMoveSym)
		colWin = checkSectionForWin(colSection, nToWin, self.lastMoveSym)
		neWin = checkSectionForWin(neSection, nToWin, self.lastMoveSym)
		seWin = checkSectionForWin(seSection, nToWin, self.lastMoveSym)

		return rowWin or colWin or neWin or seWin

	# check if state is tie (if all positions filled)
	def isTie(self):
		for c in range(0, len(self.board[0])):
			if self.board[0][c] == None:
				return False
		return True

	# get list of successors of a state, using moves of a given symbol only
	def getSuccessors(self, symbolOfMove):
		pass