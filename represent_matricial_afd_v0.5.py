class Array:
	def __init__(self, row,column,initial,final,delta):
		self.row = row
		self.column = column
		self.initial = initial
		self.final = final
		self.delta = delta
		self.array_pi = []
		self.array_final = []
		self.array_a = []
		self.array_b = []
	
	def get_array_pi(self):
		return self.array_pi
	def get_array_final(self):
		return self.array_final
	def get_array_a(self):
		return self.array_a
	def get_array_b(self):
		return self.array_b	

	def create_array_pi(self):
		element = 1
		new_row = []
		for i in range(self.row):
			if i == self.initial:
				element = 1
			else:
				element = 0
			new_row.append(element)
		self.array_pi.append(new_row)

	def create_array_final(self):
		element = 0
		for i in range(self.row):
			row = []
			for j in range(1):
				row.append(0)
			self.array_final.append(row)
		
		for numb in self.final:
			self.array_final[numb][0] = 1;
		

	def create_array_a(self):
		for i in range(self.row):
			row = []
			for j in range(self.column):
				row.append(0)
			self.array_a.append(row)

		for i in range(self.row):
			for j in range(self.column):
				if 0 == self.delta[i][j]:
					self.array_a[i][j] = 1



	def create_array_b(self):
		for i in range(self.row):
			row = []
			for j in range(self.column):
				row.append(0)
			self.array_b.append(row)


		for i in range(self.row):
			for j in range(self.column):
				if 1 == delta[i][j]:
					self.array_b[i][j] = 1


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

def computar_palavra(array,char):
	print('ola')

def computar_resultado(array,array_char):
	parcela1 = multiply_arrays(array.get_array_pi(),array_char)
	resultado_computacao = multiply_arrays(parcela1,array.get_array_final())
	return resultado_computacao[0][0]
	
def verificar_final(final):
	cont = 0
	for i in range(len(final)):
		if final[i] < states and final[i] >= 0:
			cont += 1
	if cont != len(final):
		SystemExit

states = 2
initial = 0
final = [1]
delta = [[0,1],[0,1]]
word = 'aabbab'
char = separate_word(word)

verificar_final(final)

if len(final) != 0 and (initial < states and initial >= 0) and len(delta) == states:
	array_1 = Array(states,2,initial,final,delta)
	array_1.create_array_pi()
	array_1.create_array_final()
	array_1.create_array_a()
	array_1.create_array_b()

	
	resultado = computar_resultado(array_1,[[0,1],[0,1]])
	if resultado:
		print('ACEITA')
	elif not(resultado):
		print('REJEITA')

else:
	print('REJEITA')
