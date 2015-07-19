from solution import Solution
from search_method import AStar
from heuristic_estimate import *

class AStarSolution_H1(Solution):
	"""Searching with A* algorithm with Heuristic Function: G + H1
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "A*"
		self.heuristic_estimate = "H1()     (Counting Out Of Placed Tiles)"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(AStar(H1()))

class AStarSolution_H2(Solution):
	"""Searching with A* algorithm with Heuristic Function: G + H2
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "A*"
		self.heuristic_estimate = "H2()     (Manhattan Distance Of Tiles Out Of Place)"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(AStar(H2()))

class AStarSolution_H3(Solution):
	"""Searching with A* algorithm with Heuristic Function: G + H3
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "A*"
		self.heuristic_estimate = "H3()     (Manhattan Distance + 2 * Number Of Linear Conflict)"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(AStar(H3()))
		