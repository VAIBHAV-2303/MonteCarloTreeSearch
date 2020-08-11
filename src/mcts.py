'''

MCTS algo class definition

author: @vaibhav.garg
date: 4th Aug'20
'''

import time
import random
from math import *
from copy import *

class Node():

	def __init__(self, parent, state, reachMove):

		self.totalSimulations = 0
		self.score = 0
		self.children = []
		self.parent = parent
		self.state = state
		self.reachMove = reachMove

	def expand(self):

		nextMoves, nextSymbol = self.state.getValidMoves(self.reachMove)
		for move in nextMoves:
			newBoard = deepcopy(self.state)
			newBoard.playMove(move, nextSymbol)

			newNode = Node(self, newBoard, move)
			self.children.append(newNode)

	def backPropogate(self, result):

		self.totalSimulations += 1
		self.score += result
		
		if self.parent != None: # Non-Root node
			self.parent.backPropogate(result)

	def getExplorationTerm(self):

		return sqrt(log(self.parent.totalSimulations)/(self.totalSimulations or 1))

	def getExploitationTerm(self):

		return self.score/(self.totalSimulations or 1)


class MCTS():
	
	def __init__(self, symbol, C=sqrt(2), compTime=2):

		self.symbol = symbol
		self.C = C
		self.compTime = compTime # In seconds
		self.opponentMap = {
			'X': 'O',
			'O': 'X'
		}

	def simulate(self, board, prevMove):

		currState = board.getState()

		if currState[0] == 'N':
			nextMoves, nextSymbol = board.getValidMoves(prevMove)

			# Randmoly choose the next move
			randomMove = random.choice(nextMoves)
			board.playMove(randomMove, nextSymbol)

			return self.simulate(board, randomMove)
		else:
			if currState[0] == 'W':
				if currState[1] == self.symbol:
					return 1 # Win
				else:
					return -1 # Loss
			else:
				return 0 # Draw

	def selection(self, currNode, symbol):

		curState = currNode.state.getState()
		if curState[0] != 'N': # Terminal node
			return currNode

		if len(currNode.children) == 0: # Not expanded
			return currNode

		# Selecting best child based on exploration Term and exploitation term
		if symbol == self.symbol:
			sortedChildren = sorted(currNode.children, key=lambda child: child.getExploitationTerm() + self.C*child.getExplorationTerm(), reverse=True)
		else:
			sortedChildren = sorted(currNode.children, key=lambda child: -child.getExploitationTerm() + self.C*child.getExplorationTerm(), reverse=True)

		return self.selection(sortedChildren[0], self.opponentMap[symbol])

	def getMove(self, board, prevMove):

		# Creting a root node
		rootNode = Node(None, deepcopy(board), prevMove)

		# Monte Carlo Iterations
		startTime = time.time()
		while time.time() - startTime < self.compTime:

			selectedNode = self.selection(rootNode, self.symbol) # Selection step

			if selectedNode.totalSimulations == 0: # First simulation
				result = self.simulate(deepcopy(selectedNode.state), selectedNode.reachMove)
				selectedNode.backPropogate(result)
			else: # Expansion
				selectedNode.expand()

		# Final move selection
		sortedChildren = sorted(rootNode.children, key=lambda child: child.getExploitationTerm(), reverse=True)
		
		return sortedChildren[0].reachMove
