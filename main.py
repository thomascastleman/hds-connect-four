
from util import Symbol
from game import ConnectNGame
from human import Human

def main():

	p1 = Human(Symbol.X)
	p2 = Human(Symbol.O)
	g = ConnectNGame(4, 6, 7, p1, p2)

	g.initiateGame()

if __name__ == "__main__":
	main()