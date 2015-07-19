class HeuristicEstimate(object):
	"""Interface class: HeuristicFunction
	"""
	def h(self, current_node, target_state):
		pass

class H1(HeuristicEstimate):
	def h(self, current_node, target_state):
		"""counting the tiles out of place
		   return the number of tiles that are out of place
		"""
		count = 0
		for i in range(9):
			if current_node.state.data[i] != target_state.data[i]:
				count += 1
		return count

class H2(HeuristicEstimate):
	def __stringToInt(self, array_1D):
			new_array = []
			for element in array_1D:
				if element == 'x':
					new_array.append(0)
				else:
					new_array.append(int(element))
			return new_array

	def __twoDimension(self, array_1D):
		"""Convert GameTreeNode.state.data from 1-dimension array to 2-dimension array
		"""
		L1 = array_1D[0:3]
		L2 = array_1D[3:6]
		L3 = array_1D[6:]
		array_2D = [L1,L2,L3]
		return array_2D

	def __ijIndex(self, array_2D, value):
		"""find out the position of a given node
		"""
		i = 0
		j = 0
		for x in range (0,3):
			if value in array_2D[x]:
				j = array_2D[x].index(value)
				break
			else:
				i+=1
		ijindex = [i,j]
		return ijindex

	def h(self, current_node, target_state):
		"""computing the distances of tiles out of places
		   return an integer representing the distances
		"""
		C_1D = self.__stringToInt(current_node.state.data)
		T_1D = self.__stringToInt(target_state.data)
		C = self.__twoDimension(C_1D)
		T = self.__twoDimension(T_1D)
		h_value = 0
		for x in range(0,9):
			C_index = self.__ijIndex(C,x)
			T_index = self.__ijIndex(T,x)
			h_value += abs(C_index[0]-T_index[0])+abs(C_index[1]-T_index[1])
		return h_value

class H3(HeuristicEstimate):
	def __stringToInt(self, array_1D):
			new_array = []
			for element in array_1D:
				if element == 'x':
					new_array.append(0)
				else:
					new_array.append(int(element))
			return new_array

	def __twoDimension(self, array_1D):
		"""Convert GameTreeNode.state.data from 1-dimension array to 2-dimension array
		"""
		L1 = array_1D[0:3]
		L2 = array_1D[3:6]
		L3 = array_1D[6:]
		array_2D = [L1,L2,L3]
		return array_2D

	def __ijIndex(self, array_2D, value):
		"""find out the position of a given node
		"""
		i = 0
		j = 0
		for x in range (0,3):
			if value in array_2D[x]:
				j = array_2D[x].index(value)
				break
			else:
				i+=1
		ijindex = [i,j]
		return ijindex

	def __linearConflict(self, array_2D_1, array_2D_2):
	    LinearConflict = 0
	    for x in range(0,3):
	        counter = 0
	        temp = []
	        for y in range(0,3):
	            if array_2D_1[x][y] in array_2D_2[x]:
	                temp.append(array_2D_1[x][y])
	                counter += 1
	        if counter == 2 :
	            G1 = array_2D_2[x].index(temp[0])
	            G2 = array_2D_2[x].index(temp[1])
	            L1 = array_2D_1[x].index(temp[0])
	            L2 = array_2D_1[x].index(temp[1])
	            if (G1-G2>0 and L1-L2<0) or (G1-G2<0 and L1-L2>0):
	                LinearConflict += 1
	        if counter == 3:
	            G1 = array_2D_2[x].index(temp[0])
	            G2 = array_2D_2[x].index(temp[1])
	            G3 = array_2D_2[x].index(temp[2])
	            L1 = array_2D_1[x].index(temp[0])
	            L2 = array_2D_1[x].index(temp[1])
	            L3 = array_2D_1[x].index(temp[2])
	            if (G1-G2>0 and L1-L2<0) or (G1-G2<0 and L1-L2>0):
	                LinearConflict += 1
	            if (G1-G3>0 and L1-L3<0) or (G1-G3<0 and L1-L3>0):
	                LinearConflict += 1
	            if (G3-G2>0 and L3-L2<0) or (G3-G2<0 and L3-L2>0):
	                LinearConflict += 1
	    return LinearConflict

	def __flip (self, array_2D):
		L1 = [array_2D[0][0],array_2D[1][0],array_2D[2][0]]
		L2 = [array_2D[0][1],array_2D[1][1],array_2D[2][1]]
		L3 = [array_2D[0][2],array_2D[1][2],array_2D[2][2]]
		flipped_array_2D = [L1,L2,L3]
		return flipped_array_2D

	def __h_distance(self, array_2D_1, array_2D_2):
		"""computing the distances of tiles out of places
		   return an integer representing the distances
		"""
		h_value = 0
		for x in range(0,9):
			C_index = self.__ijIndex(array_2D_1,x)
			T_index = self.__ijIndex(array_2D_2,x)
			h_value += abs(C_index[0]-T_index[0]) + abs(C_index[1]-T_index[1])
		return h_value
	
	def h(self, current_node, target_state):
		"""Calculate the number of LinearConflict
		   return LinearConflict * 2 + distances of tiles out of places
		"""
		C_1D = self.__stringToInt(current_node.state.data)
		T_1D = self.__stringToInt(target_state.data)
		C = self.__twoDimension(C_1D)
		T = self.__twoDimension(T_1D)
		h_value = self.__h_distance(C, T)
		conflict = self.__linearConflict(C,T)
		C = self.__flip(C)
		T = self.__flip(T)
		conflict += self.__linearConflict(C,T)
		h_value += conflict * 2
		return h_value







