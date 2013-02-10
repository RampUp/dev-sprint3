# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Jackie Gushue

import string

def has_no_e(word):
	e_count = string.count(word, 'e')
	if e_count == 0:
		return True
	else:
		return False

def avoids(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True

def uses_only(word, contains):
	for letter in word:
		if letter not in contains:
			return False
	return True

infile = open('words.txt', 'rU')

count_words = 0
count_e = 0
count_forbid = 0
forbidden = raw_input("Enter string of forbidden letters:  ")

for line in infile:
	count_words += 1
	word = line.strip()
	if has_no_e(word):
		count_e += 1
	if avoids(word, forbidden):
		count_forbid += 1

print "No \'e\' words percentage = " + str((float(count_e) / count_words)*100) + "."
print str(count_forbid) + " words do NOT contain any forbidden letters."







