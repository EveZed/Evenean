import itertools

# Predefine
numbers = [1,2,3,4]
letters = ['A','B','C','D']
p = 0
count = 0
choices = []

# Open the result output file
with open('results_of_latin_squares.txt','w') as file:
	file.write('all possible arrangements of numbers(4*4):')

for pe in itertools.permutations(numbers):
	exec('arrangement%s = pe'%p)
	p += 1
for letter in letters:
	for number in numbers:
		choice = f'{letter}{number}'
		choices.append(choice)

# Evaluate numbers
for i in range(24):
	exec('row0 = arrangement%s[:]'%i)
	for j in range(24):
		exec('row1 = arrangement%s[:]'%j)
		for k in range(24):
			exec('row2 = arrangement%s[:]'%k)
			for l in range(24):
				exec('row3 = arrangement%s[:]'%l)
				column0 = []
				column1 = []
				column2 = []
				column3 = []
				for m in range(4):
					for n in range(4):
						exec('copy = row%s[n]'%m)
						exec('column%s.append(copy)'%n)
				if set(numbers).issubset(set(column0)):
					if set(numbers).issubset(set(column1)):
						if set(numbers).issubset(set(column2)):
							if set(numbers).issubset(set(column3)):
								output1 = f'\n{row0}\n{row1}\n{row2}\n{row3}'
								print(output1)
								with open('results_of_latin_squares.txt','a') as file:
									file.write(output1)
									file.write('\n--------------------')
								count += 1
								exec('num_arrange%s = []'%count)
								for r in range(4):# row
									for s in range(4):# column
										exec('move = row%s[s]'%r)
										exec('num_arrange%s.append(move)'%count)

# Combined check
count2 = 0
with open('results_of_latin_squares.txt','a') as file:
	file.write('\nall possible arrangements of complete latin squares(4*4):')
for t in range(1,count+1):
	for u in range(1,count+1):
		total_arrange = []
		for v in range(16):
			exec('decade = num_arrange%s[v]'%t)
			exec('bit = num_arrange%s[v]'%u)
			if decade == 1:
				decade = 'A'
			elif decade == 2:
				decade = 'B'
			elif decade == 3:
				decade = 'C'
			else:
				decade = 'D'
			combine = f'{decade}{bit}'
			total_arrange.append(combine)
		if set(choices).issubset(set(total_arrange)):
			totalrow_0 = total_arrange[0:4]
			totalrow_1 = total_arrange[4:8]
			totalrow_2 = total_arrange[8:12]
			totalrow_3 = total_arrange[12:16]
			output2 = f'\n{totalrow_0}\n{totalrow_1}\n{totalrow_2}\n{totalrow_3}'
			print(output2)
			with open('results_of_latin_squares.txt','a') as file:
				file.write(output2)
				file.write('\n--------------------')
			count2 += 1

# Output results
mes1 = f'\ntotal arrangements of numbers:{count}'
mes2 = f'\ntotal arrangements of numbers and letters:{count2}'
print(mes1)
print(mes2)
with open('results_of_latin_squares.txt','a') as file:
	file.write(mes1)
	file.write(mes2)
