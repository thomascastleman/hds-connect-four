
from util import Symbol
from game import ConnectNGame
from human import Human
from ai import AI



# DEBUG
from util import *

def main():

	p1 = Human("Todd", Symbol.X)
	p2 = AI("Billy Boy", Symbol.O, 5)
	g = ConnectNGame(5, 10, 10, p1, p2)

	g.initiateGame()

	# p1 = Human("Todd 0", Symbol.X)
	# p2 = Human("Todd 1", Symbol.O)
	# g = ConnectNGame(3, 10, 10, p1, p2)

	# g.initiateGame()

	# board = [
	# 	[None, None, None, 0],
	# 	[1, 	0, 	None,  1],
	# 	[0, 	0,  1,     1],
	# 	[1, 	1,  1, 	   0]
	# ]	

	# """
	# NE : 
	# 0, 0, None
	# 1, 0, None, 0
	# 1, 1, 1

	# SE:
	# 1, None, None
	# 0, 1, 0, None
	# 1, 0, 1

	# """


	# n = 3
	# sym = 1

	# from util import minMovesFromWin

	# minMovesFromWin(board, n, sym)






if __name__ == "__main__":
	main()