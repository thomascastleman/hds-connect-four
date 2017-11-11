
import state

class ConnectNGame():

	def __init__(self, _n, _rows, _cols, _player1, _player2):

		self.n = _n
		self.rows = _rows
		self.cols = _cols
		self.player1 = _player1
		self.player2 = _player2

	def initiateGame(self):
		pass

	def getInitState(self):
		s = state.State(None, None, None)
		s.constructInitState(self.rows, self.cols)
		return s