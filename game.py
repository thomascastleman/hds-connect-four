
class ConnectNGame(object):

	def __init__(self, _n, _rows, _cols, _player1, _player2):

		self.n = _n
		self.rows = _rows
		self.cols = _cols
		self.player1 = _player1
		self.player2 = _player2

	# commence game 
	def initiateGame(self):
		self.currentState = self.getInitState()

		players = [self.player1, self.player2]
		winner = None
		tie = False

		while True:

			for player in players:
				self.solicitMoveFromPlayer(player)
				self.currentState.logState()

				if self.currentState.isWin(self.n):
					winner = player
					break
				elif self.currentState.isTie():
					tie = True
					break


			if winner != None:
				print winner.name, " wins."
				break
			elif tie:
				print "Tie."
				break

	# get player decision and update board
	def solicitMoveFromPlayer(self, player):
		import state
		move = player.getMove(self.currentState)
		self.currentState = state.State(self.currentState.board, move, player.symbol)

	# populate initial state based on game criteria
	def getInitState(self):
		import state
		s = state.State(None, None, None)
		s.board = []
		s.lastMoveSym = None
		s.moveFromPrev = None

		for r in range(0, self.rows):
			s.board.append([])
			for c in range(0, self.cols):
				s.board[r].append(None)

		return s