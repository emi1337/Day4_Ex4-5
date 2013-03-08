
import string

book = open("twain.txt")
text = book.read()

alphabet = string.lowercase

counter = 0

#for x in range(0,26):
#	d["string{0}".format(x)]="Hello"


for letter in alphabet:
	for char in text: 
		if char == letter: 	#reads one letter of the book at a time
			counter += 1
	print "There are %d occurrences of the letter %s" % (counter, letter)


# 1. we could loop through the entire text 26 times, just printing whenever we had the final total
# 2. We could keep separate coun ters for each letter, so that at the end you'd just have a loop
# that printed the letter of the alphabet with the 

#for letter in alphabet:
#    globals()['count' + str(letter)] = 0
#print counta