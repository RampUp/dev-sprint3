# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Chris Van Schyndel

# Exercise 8.12

def rot_x(astring, rotator):
	alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
	newstring = ''
	for letter in astring:
		if letter in alpha_upper:
			newletter = alpha_upper[(alpha_upper.find(letter) + rotator) % 26]
			newstring += newletter
		if letter in alpha_lower:
			newletter = alpha_lower[(alpha_lower.find(letter) + rotator) % 26]
			newstring += newletter
	return newstring

print rot_x('cheer', 7)
print rot_x('melon', -10)


