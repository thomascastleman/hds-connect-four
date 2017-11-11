
import util, game, player

def main():
	p1 = player.Player(util.Symbol.X)
	p2 = player.Player(util.Symbol.O)
	g = game.ConnectNGame(2, 5, 5, p1, p2)

	init = g.getInitState()
	init.logState()



if __name__ == "__main__":
	main()