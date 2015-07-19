from game_tree_node import GameTreeNode
from eight_puzzle_game_state import EightPuzzleGameState

class Solution(object):
	"""Finding the solution of the game.
	   _initial_node which is an instance of GameTreeNode represent the initial node
	   _target_state which is an instance of EightPuzzleGameState represent the target state
	   _solution_path which is a list of GameTreeNode from initial node to the target node
	   _elapsed_time contains the time(sec) a sepcific algorithm spent to find the target node
	"""

	__slots__ = {'_initial_node','_target_state','_solution_path','_elapsed_time','_target_node'}

	def __init__(self, game_state_as_array):
		self._initial_node = GameTreeNode(game_state_as_array, None)
		self._target_state = EightPuzzleGameState(['1','2','3','4','5','6','7','8','x'])
		self._solution_path = []
		self._elapsed_time = None
		self._target_node = None

	def setSearchMethod(self, search_method):
		self.searchMethod = search_method

	def performSearchMethod(self):
		self._target_node, self._elapsed_time = self.searchMethod.search(self._initial_node, self._target_state)

	def countStep(self):
		"""return the number of steps from begining to the target node
		"""
		if self._target_node:
			current_node = self._target_node
			while current_node.state.data != self._initial_node.state.data:
				self._solution_path.append(current_node.state.representation)
				current_node = current_node.parent
			self._solution_path.append(self._initial_node.state.representation)
			return len(self._solution_path) - 1
		else:
			return 0

	def showPath(self):
		"""Show the path from initial node to target node in report
		"""
		solution_path = self._solution_path[::-1]
		size = len(solution_path)
		counter = 0
		G1 = []
		G2 = []
		G3 = []
		while size >= 0:
			L1 = []
			L2 = []
			L3 = []
			if size >= 5:
				for x in range(0,5):
					L1.append(solution_path[counter+x][0:3])
					L2.append(solution_path[counter+x][3:6])
					L3.append(solution_path[counter+x][6:])
				counter += 5
				size -= 5
				G1.append(L1)
				G2.append(L2)
				G3.append(L3)
			else:
				for x in range(0,size):
					L1.append(solution_path[counter+x][0:3])
					L2.append(solution_path[counter+x][3:6])
					L3.append(solution_path[counter+x][6:])
				counter += 5
				size -= 5
				G1.append(L1)
				G2.append(L2)
				G3.append(L3) 
		str1 = ""
		str2 = ""
		str3 = ""
		for x in range(0,len(G1)):
			for y in range(0,len(G1[x])):
				str1 += G1[x][y]
				str1 += "      "
				str2 += G2[x][y]
				str2 += "  =>  "
				str3 += G3[x][y]
				str3 += "      "
		str1.strip()
		str2 = str2[0:len(str2)-5]
		str3.strip()
		G = ""
		i = 0
		while i<len(str1):
			G += str1[i:i+45]
			G += "\n"
			G += str2[i:i+45]
			G += "\n"
			G += str3[i:i+45]
			G += "\n"
			G += "\n"
			i += 45
		return G

	@property
	def initial_node(self):
		"""Gets the initial node"""
		return self._initial_node

	@property
	def target_state(self):
		"""Gets the target state for this game"""
		return self._target_state

	@property
	def solution_path(self):
		"""Gets nodes of the solution path"""
		return self._solution_path

	@property
	def elapsed_time(self):
		"""Gets the elapsed time"""
		return self._elapsed_time

	@property
	def target_node(self):
		"""Gets the target node"""
		return self._target_node
