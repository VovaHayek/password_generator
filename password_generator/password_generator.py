import random
import os

class password_generator():
	def __init__(self, *parameters):
		self.parameters = parameters
		self.password = ''
		self.password_array = []
		self.parameter_id = 0

	#If password's lenght isn't enough, this func solve this problem
	def finish_generate(self):
		for parameter in self.parameters:
				self.parameter_id += 1
				if parameter == 'y':
					if self.parameter_id-1 == 1:
						for lenghtless_password in range((int(self.parameters[0])-len(self.password_array))):
							numbers = open(os.path.dirname(__file__) + 'numbers.txt', 'r')
							for number in numbers:
								self.password_array.append(number[random.randrange(0, len(number))])
								
					elif self.parameter_id-1 == 2:
						for lenghtless_password in range((int(self.parameters[0])-len(self.password_array))):
							uppercase_characters = open(os.path.dirname(__file__) + 'alphabet_characters.txt', 'r')
							for uc in uppercase_characters:
								self.password_array.append(uc[random.randrange(0, len(uc))])

					elif self.parameter_id-1 == 3:
						for lenghtless_password in range((int(self.parameters[0])-len(self.password_array))):
							lowercase_characters = open(os.path.dirname(__file__) + 'alphabet_characters.txt', 'r')
							for lower in lowercase_characters:
								self.password_array.append(lower[random.randrange(0, len(lower))].lower())

					elif self.parameter_id-1 == 4:
						for lenghtless_password in range((int(self.parameters[0])-len(self.password_array))):
							symbols = open(os.path.dirname(__file__) + 'special_symbols.txt', 'r')
							for symbol in symbols:
								self.password_array.append(symbol[random.randrange(0, len(symbol))])

	#Main function that generates password
	def generator(self):
		if 'y' in self.parameters:
			print(self.parameters)
		if self.parameters[2] == 'y':
			for number_of_uppercase_chrs in range(random.randrange(1, int(self.parameters[0])-2)):
				uppercase_characters = open(os.path.dirname(__file__) + 'alphabet_characters.txt', 'r')
				for uc in uppercase_characters:
					self.password_array.append(uc[random.randrange(0, len(uc))])

		if self.parameters[1] == 'y':
			for number_of_digits in range(random.randrange(1, (int(self.parameters[0])-(len(self.password_array)+2)))):
				numbers = open(os.path.dirname(__file__) + 'numbers.txt', 'r')
				for number in numbers:
					self.password_array.append(number[random.randrange(0, len(number))])

		if self.parameters[4] == 'y':
			for number_of_symbols in range(random.randrange(1, (int(self.parameters[0])-(len(self.password_array)+1)))):
				symbols = open(os.path.dirname(__file__) + 'special_symbols.txt', 'r')
				for symbol in symbols:
					self.password_array.append(symbol[random.randrange(0, len(symbol))])

		if self.parameters[3] == 'y':
			for number_of_lowercase_chrs in range((int(self.parameters[0])-len(self.password_array))):
				lowercase_characters = open(os.path.dirname(__file__) + 'alphabet_characters.txt', 'r')
				for lower in lowercase_characters:
					self.password_array.append(lower[random.randrange(0, len(lower))].lower())
		if len(self.password_array) < int(self.parameters[0]):
			self.finish_generate()
			

		random.shuffle(self.password_array)
		password = ''.join(self.password_array)
		print(password)

#Password parameters
password_lenght = input('Enter password lenght: ')
password_digits = input('Include numbers (yes = \'y\', no = \'n\'): ')
password_uppercase = input('Include uppercase latters (yes = \'y\', no = \'n\'): ' )
password_lowercase = input('Include lowercase latters (yes = \'y\', no = \'n\'): ' )
password_punctuation = input('Include symbols "!@#$%^&*?_+=-"& (yes = \'y\', no = \'n\'): ' )

#Program start
if __name__ == '__main__':
	password_generator = password_generator(password_lenght, password_digits, password_uppercase, password_lowercase, password_punctuation)
	password_generator.generator()