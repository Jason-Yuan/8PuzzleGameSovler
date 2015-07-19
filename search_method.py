import time
import random
from game_tree_node import GameTreeNode

class SearchMethod(object):
	"""Interface class: SearchMethod
	"""
	def search(self, initial_node, target_state):
		pass


class BFS(SearchMethod):
	"""Breadth-first Search Algorithm
	"""
	def search(self, initial_node, target_state):
		"""Search for the target state
		   return target_node as a GameTreeNode object and elapsed_time in second
		"""
		target_node = None
		start = time.time()
		Open = [initial_node]
		exist_node = [initial_node] 
		while Open:
			current_node = Open.pop(0)
			if current_node.state.data == target_state.data:
				target_node = current_node
				break
			else:
				current_node.generate_children()
				if current_node.children != None:
					for child in current_node.children:
						flag = 0
						for node in exist_node:
							if node.state.data == child.state.data:
								flag = 1
						if flag == 0:
							Open.append(child)
							exist_node.append(child)
		end = time.time()
		elapsed_time = end - start
		return target_node, elapsed_time


class DescentHillClimbing(SearchMethod):
	"""Descent Hill Climbing Search Algorithm
	"""
	__slot__ = {'_g_value', '_h_value'}

	def __init__(self, heuristic_estimate):
		self.heuristicEstimate = heuristic_estimate

	def g(self, current_node, initial_node):
		"""the distance from the start to current state
		   return an integer repersenting the distance
		"""
		count = 0
		while current_node.state.data != initial_node.state.data:
			count += 1
			current_node = current_node.parent
		return count

	def search(self, initial_node, target_state):
		"""Search for the target state
		   return target_node as a GameTreeNode object and elapsed_time in second
		"""
		c = 0
		initial_node.value = self.g(initial_node, initial_node) + self.heuristicEstimate.h(initial_node, target_state)
		target_node = None
		start = time.time()
		if initial_node.state.data == target_state.data:
			target_node = initial_node
		else:
			initial_node.generate_children()
			children_list = []
			for child in initial_node.children:
				child.value = self.g(child, initial_node) + self.heuristicEstimate.h(child, target_state)
				children_list.append(child)
			exist_node = children_list
			current_node = initial_node
			while children_list:
				children_list = sorted(children_list)
				# Choose a best child if best child is better than current node otherwise randomly choose a child 
				if current_node > children_list[0]:
					# Choose which child as the next step
					if (len(children_list) == 1) or children_list[0] < children_list[1]:
						current_node = children_list[0]
					else:
						temp = []
						for child in children_list:
							if child == children_list[0]:
								temp.append(child)
						index = random.randint(0,len(temp)-1)
						current_node = temp[index]
				else: #current_node <= children_list[0]
					index = random.randint(0,len(children_list)-1)
					current_node = children_list[index]

				# If this child is not the solution, gentrate children of this child	
				if current_node.state.data == target_state.data:
					target_node = current_node
					break
				else:
					current_node.generate_children()
					if current_node.children != None:
						for child in current_node.children:
							flag = 0
							for node in exist_node:
								if node.state.data == child.state.data:
									flag = 1
							if flag == 0:
								child.value = self.g(child, initial_node) + self.heuristicEstimate.h(child, target_state)
								c = c + 1
								children_list.append(child)
								exist_node.append(child)				
		end = time.time()
		elapsed_time = end - start
		return target_node, elapsed_time


class AStar(SearchMethod):
	"""A* Search Algorithm
	"""
	__slot__ = {'_g_value', '_h_value'}

	def __init__(self, heuristic_estimate):
		self.heuristicEstimate = heuristic_estimate

	def g(self, current_node, initial_node):
		"""the distance from the start to current state
		   return the distance
		"""
		count = 0
		while current_node.state.data != initial_node.state.data:
			count += 1
			current_node = current_node.parent
		return count

	def search(self, initial_node, target_state):
		"""Search for the target state
		   return target_node as a GameTreeNode object and elapsed_time in second
		"""
		c = 0
		target_node = None
		start = time.time()
		exist_node = [initial_node]
		Open = [initial_node]
		while Open:
			Open = sorted(Open)
			current_node = Open.pop(0)
			if current_node.state.data == target_state.data:
				target_node = current_node
				break
			else:
				current_node.generate_children()
				if current_node.children != None:
					for child in current_node.children:
						flag = 0
						for node in exist_node:
							if node.state.data == child.state.data:
								flag = 1
						if flag == 0:
							child.value = self.g(child, initial_node) + self.heuristicEstimate.h(child, target_state)
							c = c + 1
							Open.append(child)
							exist_node.append(child)
		end = time.time()
		elapsed_time = end - start
		return target_node, elapsed_time
		