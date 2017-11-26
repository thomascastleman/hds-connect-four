
class ConnectNGame(object):

	def __init__(self, _n, _rows, _cols, _player1, _player2):

		# protect against illegal game parameters
		if _n > 0 and _rows > 0 and _cols > 0 and (_n < _rows or _n < _cols):
			self.n = _n
			self.rows = _rows
			self.cols = _cols
			self.player1 = _player1
			self.player2 = _player2

			self.player1.game = self
			self.player2.game = self
		else:
			print "\nILLEGAL GAME ERROR\n"
			sys.exit()

	# commence game 
	def initiateGame(self):
		self.currentState = self.getInitState()

		players = [self.player1, self.player2]
		winner = None
		tie = False

		while True:

			for player in players:

				self.currentState.logState()
				self.solicitMoveFromPlayer(player)

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
		print "\n" + player.name + "'s move:"
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