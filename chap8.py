# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Jackie Gushue

# Question 8.12 ROT13 (weak form of encryption)
# After writing code and checking answer, realized
# need to take into account upper vs. lower case letters

def char_to_num(word, index):
	num_list = []
	for char in word:
		num_list.append(ord(char)+index)
	return num_list

def num_to_char(num_list):
	word = ""
	for num in num_list:
		word = word + chr(num)
	return word

def rotate_word(word, index):
	return num_to_char(char_to_num(word, index))

print rotate_word("cheer", 7)

# Correct answer

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
        print "Start: " + str(start)
    elif letter.islower():
        start = ord('a')
        print "Start: " + str(start)
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print rotate_word('cheer', 7)
    print rotate_word('melon', -10)
    print rotate_word('sleep', 9)









