
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

# determine the min number of moves to win on a board, with respect to a symbol
def minMovesFromWin(board, n, symbol):
	
	allSections = []

	# get row sections:
	for row in board:
		allSections.append(row)

	# get col sections:
	for c in range(len(board[0])):
		col = []
		for r in range(len(board)):
			col.append(board[r][c])
		allSections.append(col)

	# get northeast diagonal sections
	
	numRows = len(board)
	numCols = len(board[0])

	col = 0
	for row in range(n - 1, numRows - 1):
		r, c = row, col
		diag = []
		while r >= 0 and col < numCols:
			diag.append(board[r][c])
			r -= 1
			c += 1
		allSections.append(diag)

	row = numRows - 1
	for col in range(0, numCols - n + 1):
		r, c = row, col
		diag = []
		while r >= 0 and c < numCols:
			diag.append(board[r][c])
			r -= 1
			c += 1
		allSections.append(diag)

	# get southeast diagonal sections:

	col = numCols - 1
	for row in range(n - 1, numRows - 1):
		r, c = row, col
		diag = []
		while r >= 0 and c >= 0:
			diag.append(board[r][c])
			r -= 1
			c -= 1
		allSections.append(diag)

	row = numRows - 1
	for col in range(numCols - 1, n - 2, - 1):
		r, c = row, col
		diag = []
		while r >= 0 and c >= 0:
			diag.append(board[r][c])
			r -= 1
			c -= 1
		allSections.append(diag)
	
	minimum = None
	for section in allSections:
		num = minWinOnSection(section, n, symbol)
		minimum = num if minimum == None else num if num < minimum else minimum
	return minimum


# determine the minimum number of moves to win on a section, or None if no win
def minWinOnSection(section, n, symbol):
	minimum = None

	for i in range(len(section) - n + 1):
		nsection = section[i:i + n]
		# get num moves
		num = numFromWinOnNSection(nsection, symbol)
		# update min
		minimum = num if minimum == None else num if num < minimum else minimum

	return minimum


# determine number of moves to win on an n section, or None if no win possible
def numFromWinOnNSection(nsection, symbol):
	moves = 0
	for pos in nsection:
		if pos == None:	# add up blank positions
			moves += 1
		elif pos != symbol:	# if interrupted by other symbol, no win possible
			return None
	return moves