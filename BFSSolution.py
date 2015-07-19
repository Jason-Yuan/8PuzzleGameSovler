from solution import Solution
from search_method import BFS

class BFSSolution(Solution):
	"""Searching with Breadth-First Search algorithm
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "Breadth-First Search"
		self.heuristic_estimate = "None"
		Solution.__init__(self, game_state_as_array)
		self.setSearchMethod(BFS())
