
import state

class ConnectNGame():

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

			self.solicitMoveFromPlayer(currentState, player1)
			if currentState.isWin() or currentState.isTie():
				break

			self.solicitMoveFromPlayer(currentState, player2)
			if currentState.isWin() or currentState.isTie():
				break

	# get player decision and update board
	def solicitMoveFromPlayer(self, state, player):
		move = player.getMove(self.currentState)
		self.currentState = state.State(self.currentState.board, move, player.symbol)

	# populate initial state based on game criteria
	def getInitState(self):
		s = state.State(None, None, None)
		s.constructInitState(self.rows, self.cols)
		return s