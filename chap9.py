# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Chris Van Schyndel

# Exercise 9.1

def greaterthantwenty():
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word

# Exercise 9.2

def has_no_e(string):
	for letters in string:
		if letters == 'e' or letters == 'E':
			return False
	return True


def words_with_e():
	fin = open('words.txt')
	words_with_e = 0
	words_without_e = 0
	wordcheck = False
	for line in fin:
		word = line.strip()
		for letters in word:
			if letters == 'e':
				wordcheck = True
		if wordcheck == True:
			words_with_e += 1
			wordcheck = False
		else:
			print word
			words_without_e += 1
	return str(((words_without_e * 100) / words_with_e * 100)/100) + '%' 

# Exercise 9.3

def avoids():
	print 'Please enter in the Forbidden letters!'
	astring = raw_input('Forbidden Letters: >')
	wordcheck = False
	wordcount = 0
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		for letters in word:
			for forbiddens in astring:
				if letters == forbiddens:
					wordcheck = True
		if wordcheck == True:
			wordcheck = False
		else:
			wordcount +=1
			print word
	print wordcount

# Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
# My guess? 'zyqkj'


# Exercise 9.4

def uses_only(aword, astring):
	# Returns True if the word contains only letters in the list.
	# It must also contain all the letters from the list.
	count = 0
	aword = aword.replace(' ', '')
	letterchecker = False
	for bagels in astring:
		if bagels not in aword:
			return False
	for bagels in aword:
		for cheesecakes in astring:
			if cheesecakes == bagels:
				letterchecker = True
		if letterchecker == False:
			return False
		else:
			letterchecker = False
	return True

print uses_only('cell of heal', 'acefhlo')
