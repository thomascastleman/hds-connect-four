
from util import Symbol
from game import ConnectNGame
from human import Human

def main():

	p1 = Human("Player 1", Symbol.X)
	p2 = Human("Player 2", Symbol.O)
	g = ConnectNGame(4, 10, 10, p1, p2)

	g.initiateGame()

if __name__ == "__main__":
	main()