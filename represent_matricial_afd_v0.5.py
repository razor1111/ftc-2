class Array:
	def __init__(self, row,column,initial,final,delta):
		self.row = row
		self.column = column
		self.initial = initial
		self.final = final
		self.delta = delta
	

	def create_array_pi(self):
		array_pi = []
		element = 1
		new_row = []
		for i in range(self.row):
			if i == self.initial:
				element = 1
			else:
				element = 0
			new_row.append(element)
		array_pi.append(new_row)
		return array_pi

	def create_array_final(self):
		array_final = []
		element = 0
		for i in range(self.row):
			row = []
			for j in range(1):
				row.append(0)
			array_final.append(row)
		
		for numb in self.final:
			array_final[numb][0] = 1;
		
		return array_final

	def create_array_a(self):
		array_a = []
		for i in range(self.row):
			row = []
			for j in range(self.column):
				row.append(0)
			array_a.append(row)

		for i in range(self.row):
			for j in range(self.column):
				if 0 == delta[i][j]:
					array_a[i][j] = 1

		return array_a

	def create_array_b(self):
		array_b = []
		for i in range(self.row):
			row = []
			for j in range(self.column):
				row.append(0)
			array_b.append(row)


		for i in range(self.row):
			for j in range(self.column):
				if 1 == delta[i][j]:
					array_b[i][j] = 1

		return array_b

def multiply_arrays(array_1,array_2):
	result = []
	row_1 = len(array_1)
	row_2 = len(array_2)
	column_2 = len(array_2[0])

	for i in range(row_1):
		new_row = []
		for j in range(column_2):
			acm = 0
			for k in range(row_2):
				acm = acm + array_1[i][k] * array_2[k][j]
			new_row.append(acm)
		result.append(new_row)
	return result

def separate_word(word):
	char = []
	for i in range(len(word)):
		char.append(word[i])
	return char


states = 2
initial = 0
final = [0]
delta = [[0,1],[0,1]]
word = 'aabaab'

"""
if len(final) != 0:
	array_1 = Array(states,2,initial,final,delta)
	array_pi = array_1.create_array_pi()
	array_final = array_1.create_array_final()
	array_a = array_1.create_array_a()
	array_b = array_1.create_array_b()

	result = multiply_arrays(array_b,array_final)

	print(array_pi)
	print(array_final)
	print(array_a)
	print(array_b)

	print('\n')
	print(result)
else:
	print('REJEITA')"""