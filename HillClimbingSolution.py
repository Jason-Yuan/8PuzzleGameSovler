from solution import Solution
from search_method import DescentHillClimbing
from heuristic_estimate import *

class HillClimbingSolution_H1(Solution):
	"""Searching with Descent Hill Climbing algorithm with Heuristic Function: G + H1
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "Descent Hill Climbing"
		self.heuristic_estimate = "H1()     (Counting Out Of Placed Tiles)"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(DescentHillClimbing(H1()))

class HillClimbingSolution_H2(Solution):
	"""Searching with Descent Hill Climbing algorithm with Heuristic Function: G + H2
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "Descent Hill Climbing"
		self.heuristic_estimate = "H2()     (Manhattan Distance Of Tiles Out Of Place)"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(DescentHillClimbing(H2()))

class HillClimbingSolution_H3(Solution):
	"""Searching with Descent Hill Climbing algorithm with Heuristic Function: G + H3
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "Descent Hill Climbing"
		self.heuristic_estimate = "H3()     (Manhattan Distance + 2 * Number Of Linear Conflict)"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(DescentHillClimbing(H3()))
		