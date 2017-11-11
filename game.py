
class ConnectNGame:

	def __init__(self, _n, _rows, _cols, _player1, _player2):

		self.n = _n
		self.rows = _rows
		self.cols = _cols
		self.player1 = _player1
		self.player2 = _player2

	# commence game 
	def initiateGame(self):
		self.currentState = self.getInitState()

		while True:

			self.solicitMoveFromPlayer(self.player1)
			if self.currentState.isWin() or self.currentState.isTie():
				break

			self.solicitMoveFromPlayer(self.player2)
			if self.currentState.isWin() or self.currentState.isTie():
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
		s.constructInitState(self.rows, self.cols)
		return s