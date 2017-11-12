
import util, game

def main():
	import human

	p1 = human.Human(util.Symbol.X)
	p2 = human.Human(util.Symbol.O)
	g = game.ConnectNGame(4, 6, 7, p1, p2)

	g.initiateGame()



if __name__ == "__main__":
	main()