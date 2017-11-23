
import game
from util import inf, Symbol

class AI:

	def __init__(self, _name, _symbol, _depth):
		self.name = _name
		self.symbol = _symbol
		self.depth = _depth
		self.game = None	# reference to game that contains this AI

	# solicit move from AI
	def getMove(self, state):
		bestState = self.minimax(state, True, 1, self.depth)
		return bestState.moveFromPrev[1]	# return column of move

	# determine predicted value of state: returns (state, cost, depth)
	def minimax(self, curState, isMaximizing, depth, maxDepth):
		# check for terminal state reached:
		if curState.isWin(self.game.n):
			# if win
			if curState.lastMoveSym == self.symbol:
				return (inf.POS_INFINITY, depth)
			# if loss
			else:
				return (inf.NEG_INFINITY, depth)

		# if tie
		elif curState.isTie():
			return (0, depth)

		# if max depth reached
		elif depth == maxDepth:
			return (self.heuristic(curState), depth)

		# otherwise evaluate recursively
		else:
			children = curState.getSuccessors(self.symbol if isMaximizing else Symbol.O if self.symbol == Symbol.X else Symbol.X)
			bestState, bestCost, bestDepth = None, None, None

			for child in children:
				# calculate child cost
				state, cost, childDepth = self.minimax(child, not isMaximizing, depth + 1, maxDepth)

				if isMaximizing:
					# choose higher cost
					if cost > bestCost:
						bestState, bestCost, bestDepth = child, cost, childDepth
					elif cost == bestCost:
						# if both wins, choose shallow
						if cost == inf.POS_INFINITY:
							if childDepth < bestDepth:
								bestState, bestCost, bestDepth = child, cost, childDepth

						# if both losses, choose deep
						elif cost == inf.NEG_INFINITY:
							if childDepth > bestDepth:
								bestState, bestCost, bestDepth = child, cost, childDepth

				# if minimizing
				else:
					# choose lower cost
					if cost < bestCost:
						bestState, bestCost, bestDepth = child, cost, childDepth
					elif cost == bestCost:
						# if both wins, choose deep
						if cost == inf.POS_INFINITY:
							if childDepth > bestDepth:
								bestState, bestCost, bestDepth = child, cost, childDepth

						# if both losses, choose shallow
						elif cost == inf.NEG_INFINITY:
							if childDepth < bestDepth:
								bestState, bestCost, bestDepth = child, cost, childDepth

			return (bestState, bestCost, bestDepth)

	def heuristic(self, curState):
		pass