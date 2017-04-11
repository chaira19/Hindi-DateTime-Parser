import datetime 
from dateutil.relativedelta import *

## give final date and time after parsing by changing current date-time
def change_datetime ( c="0", y=0,  mt=0, w=0,  d=0,  h=0,  m=0,  s=0):

	#mt = mt + 12*y
	#d = d + 30*mt

	now = datetime.datetime.now()
	change = relativedelta( years =+ y, months =+ mt, weeks =+ w, days =+ d, hours =+ h, minutes =+ m, seconds =+ s)
	#print (now + change)

	if c == "date":
		return (now + change).date()

	elif c == "time":
		return (now + change).time()

## make separate date and time functions

#def change_date (y=0, m=0, w=0, d=0):
#def change_time (h=0, m=0, s=0):



## make separate functions for setting date and time and print -- if not provided the data
## give final date and time after parsing by setting date-time
def set_datetime (y=0, mt=0, d=0, h=0, m=0, s=0, c="0"):

	a = ""
	if d!=0:
		a = a + str(d) + "/"
	if mt!=0:
		a = a + str(mt) + "/"
	if y!=0:
		a = a + str(y)   

	#a = a + " "

	if h!=0:
		a = a + str(h) + ":"
	if m!=0:
		a = a + str(m) + ":"
	if s!=0:
		a = a + str(s)

	if c!="0":
		a = a + " "
		a = a + str(c)
		#print (a, "a")

	return a

## make function for am/pm

def get_disease (string):

	with open("dataset.txt") as f:
		content = f.readlines()

	names = []
	definitions = []
	values = []
	check = 1

	## TODO 
	## remove the common words from defintion (or input) (or use replace) like a, the,disease, etc. while splitting definition in words
	## Also do stemming
	## Go through dataset once manually to get these words
	for word in content:

		if word[0] == 'n':

			## TODO think better way in which pop is not required, directly append only if required
			if check == 1:

				names.append(word)
				check = 0

			if check == 0:

				names.pop()
				names.append(word) 

		if word[0] == 'd':

			definitions.append(word)
			check = 1
			values.append(0)

	#string = input("Give Text:")
	words = string.split(" ")

	for word in words:

		for defintion in definitions:

			defintion.replace('. ',' ')
			defintion.replace(', ',' ')

			definition_words = defintion.split(" ")

			if word in definition_words:

				values[definitions.index(defintion)] += 1
				#print (word)

				highest = 0
				index_of_highest = 0
				answer = []
	## TODO if there are more than one highest

	for value in values:

		if value > highest:

			highest = value
			index_of_highest = values.index(value)

	answer.append(names[index_of_highest])
	answer.append(highest)
	answer.append(definitions[index_of_highest])


	for word in words:

		newd = definitions[index_of_highest].replace('. ',' ')
		newda = newd.replace(', ',' ')

		definition_words = newda.split(" ")
		## cannot pass with or in split, find better way

		#print (definition_words)
		
		if word in definition_words:

			

			values[definitions.index(defintion)] += 1
			answer.append(word)

	#			print (definitions[index_of_highest][defintion.index(word)])

	## make definition sort only usable things
	## find a way like , and parameters for passing more than value in relplace

	return answer
	
def get_sentences(str):

	import re
	## use of regular expressions
	
	## str cannot be changed further, always make a new object

	words = str.split(" ")

	Abbrs = ['Mr.', 'mr.', 'Mrs.', 'mrs.', 'Dr.', 'dr.' , 'Er.', 'er.', 'Prof.', 'prof.', 'Br.', 'br.', 'Fr.', 'fr.', 'Sr.', 'sr.', 'Jr.', 'jr.']
	SentenceType = []

	for abbr in Abbrs:

		if abbr in words:
			new_word = abbr.replace(abbr[len(abbr)-1], "")
			str = str.replace(abbr, new_word)
			#print (new_str)

			## str.replace(abbr[len(abbr)-1], " ")
			## Do directly in string without using words

	for word in words:

		if re.findall(r'\.(.)+\.', word):
			
			new_word = word.replace('.','')
			str = str.replace(word, new_word)
			#print (word)
			#print (new_word)
			#print (new_str2)

		if '.' in word[0:len(word)-2]:

			new_word = word.replace('.', '[dot]')
			str = str.replace(word, new_word)

	for letter in str:

		if letter == '.':
			SentenceType.append("Assertive")

		if letter == '?':
			SentenceType.append("Interrogative")

		if letter == '!' or letter == '!!':
			SentenceType.append('Exclamatory')

	sentences = re.split("[ ]*[.|?|!|!!]+[ ]*", str)

	if (str[len(str)-1] == '.') or (str[len(str)-1] == '?') or (str[len(str)-1] == '!'):

		sentences.pop()
	
	return dict(zip(sentences, SentenceType))

	## TODOs
	## Extend Abbrs list
	## Dots back in sentences
	## If abbr of acronyms with dots at end of a sentence?
	## what if sentence doesn't end with !!? Get the expression from this word.
	## If already a new line exist.
	## Also implement through machine learning to obtain results without help of punctuation.
	## Sentence Type : What about Imperative, compound, complex etc. Exclamatory Sentence or Word
	## ensure sentences are returned sequentially

def get_tokens(str):

	words = str.split(" ")

	return words

	## Make an algorithm for different kind of words for forming effective tokens before returning


























