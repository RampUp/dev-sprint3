# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Andrew Lee

#9.1

#def print_20(file):
#	fin = open(file)
#	for line in fin:
#		word = line.strip()
#		if len(word) > 20:
#			print word


#9.2

def has_no_e(word):
	if word.count('e') == 0:
		return True
	else:
		return False

def print_no_e(file):
	fin = open(file)
	count_e = 0
	count_no_e = 0
	for line in fin:
		word = line.strip()
		if has_no_e(word) == True:
			print word
			count_no_e += 1
		else:
			count_e += 1
	percent_no_e = float(count_no_e)/float(count_e + count_no_e)
	print count_no_e, 100*percent_no_e

#print_no_e('words.txt')


#9.3
def avoid(word, forbid):
	for letter in forbid:
		if word.count(letter) == 0:
			continue
		else:
			return False
	return True

#print avoid('Andrew', 'zwyxcs')

def avoid_list(file, forbid):
	fin = open(file)
	count = 0
	for line in fin:
		word = line.strip()
		if avoid(word, forbid) == True:
			print word
			count += 1
	print count

#avoid_list('words.txt', 'aeiou')

def uses_only(word, contained):
	for letter in word:
		if letter not in contained:
			return False
	return True

print uses_only('bugger', 'gul')





		