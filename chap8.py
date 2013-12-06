# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Andrew Lee

#8.12

def rotate_word(word, rotate):
	for letter in word:
		if letter.isupper():
			start = 65
		elif letter.islower():
			start = 97
		else:
			return letter

		n = ord(letter) - start
		x = (n+rotate) % 26 + start
		new = chr(x)
		print new,

rotate_word('melon', -10)




#8.1

#def trav(fruit):
#	index = 0
#	while index < len(fruit):
#		letter = fruit[index]
#		print letter,
#		index = index + 1

#def back_trav(fruit):
#	index = -1
#	while abs(index) < len(fruit) + 1:
#		letter = fruit[index]
#		print letter,
#		index = index - 1

#trav('Andrew')


#back_trav('Andrew')

#def loop_trav(fruit):
#	for char in fruit:
#		print char,

#loop_trav('Andrew')


#8.2

#def concat():
#	prefixes = 'JKLMNOPQ'
#	suffix = 'ack'
#	for letter in prefixes:
#		if letter in ('O', 'Q'):
#			print letter + 'u' + suffix
#		else:
#			print letter + suffix

#concat()

#8.3
#fruit[:] will go from the beginning to the end

#8.4
#def find(word, letter, start):
#	index = 0
#	while index + start < len(word):
#		if word[start:index] == letter:
#			return index
#		index = index + 1
#	return -1

#find('Andrew', 'A', 0)

#8.5-8.6
#def letter_count(word, win, start):
#	count = 0
#	for letter in word[start:]:
#		if letter == win:
#			count = count + 1
#	print count

#letter_count('Andrew', 'n', 0)

#8.7
#fruit = 'banana'
#fruit.count('a')

#8.9
#def is_reverse(word1,word2):
#	if len(word1) != len(word2):
#		return False

#	i = 0
#	j = len(word2) - 1

#	while j > -1:
#		print i,j

#		if word1[i] != word2[j]:
#			return Flase
#		i = i + 1
#		j = j - 1

#	return True

#is_reverse('pots', 'stop')

