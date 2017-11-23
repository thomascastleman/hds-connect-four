
# types of player symbols to their numeric equivalents for board serialization
class Symbol:
	O = 0
	X = 1

class inf:
	POS_INFINITY = float('inf')
	NEG_INFINITY = float('-inf')

# deep copies a board
def copyBoard(board):
	newBoard = []
	for r in range(0, len(board)):
		newBoard.append([])
		for c in range(0, len(board[r])):
			newBoard[r].append(board[r][c])
	return newBoard

# check an extracted section of the board for wins of a given symbol
def checkSectionForWin(section, nToWin, symbol):
	inARow = 0
	for pos in section:
		inARow = inARow + 1 if pos == symbol else 0	# tally up symbols found in row

		if inARow == nToWin:	# if n in a row reached
			return True
	return False