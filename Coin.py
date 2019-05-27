import random

number_of_tests = 1000
number_of_flips = 1000

tests = 0

with open ('C:\\Users\\dmitr\\Documents\\GitHub\\Learning-Games\\coin_output.txt', 'w') as output_file:

	while tests < number_of_tests:
		flips = 0
		heads = 0
		
		while flips < number_of_flips:
			if random.randint(0,1):
				heads = heads + 1
			flips = flips + 1	

		new_line = str(tests+1) + '\t' + str(heads) + '\n'
		output_file.write(new_line)

		print('In the test #' + str(tests+1) + ' heads has come up ' + str(heads) + ' times.' )	
		tests = tests + 1