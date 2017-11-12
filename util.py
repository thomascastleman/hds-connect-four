
# types of player symbols to their numeric equivalents for board serialization
class Symbol:
	O = 0
	X = 1

# deep copies a board
def copyBoard(board):
	newBoard = []
	for r in range(0, len(board)):
		newBoard.append([])
		for c in range(0, len(board[r])):
			newBoard[r].append(board[r][c])
	return newBoard