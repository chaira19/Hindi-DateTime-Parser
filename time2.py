import datetime 

## get the input
string = input("Give the text:")

## convert inpurt to lower case
string = string.lower()

## split the input into words(list)
words = string.split(" ")

## give final date and time after parsing
def answer ( y=0,  mt=0, w=0,  d=0,  h=0,  m=0,  s=0):

	mt = mt + 12*y
	d = d + 30*mt

	now = datetime.datetime.now()
	change = datetime.timedelta( weeks =w, days=d, hours = h, minutes =m, seconds = s)
	print (now + change)

## categories of words (dictionaries or associative arrays)
Date = {"aaj":"0", "kal":"1", "parson":"2", "dashak":0 "mahine":"0", "hafte":0, "din":"0","monday":"0", "tuesday":"0", "wednesday":"0", "thursday":"0", "friday":"0", "saturday":"0", "sunday":"0", "saal":"0", "somvar":0, "mangalvar":0, "budhvar":"0", "guruvar":0, "shukravar":0, "shanivar":0, "january":0, "february":0, "march":0, "april":0, "may":0, "june":0, "july":0, "august":0, "september":0, "october":0, "november":0, "december":0}
Time = {"abhi":"0", "baje":"0", "baj":0, "ghante":"0", "ghanta":"0", "subah":"0", "shaam":"0", "dopahar":"0", "raat":"0", "minutes":0, "minute":0, "seconds":"0", "second":"0"}
DateTime = {"baad":-1, "pahle":-1, "pichle":1, "agle":1, "aadhe":1, "aadha":1, "dedh":1, "dhaai":1, "saade":1, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1}
Separators = {"se":0, "aur":0, "evam":0, "lekin":0, "par":0, "magar":0, "kintu":0, "parantu":0, "ya":0, "kyunki":0, "isliye":0}

## four stacks
Stack_Date = []
Stack_Time = []
Stack_Next = []
Stack_Prev = []

## Stack used when a word of type "next" comes after a word of type "next"
temp = []

## Algorithm to fill all the words in stack
for word in words:

## if next and prev stack is empty then fill accordingly
	if len(Stack_Next)==0 and len(Stack_Prev)==0 :

		if word in Date:
			Stack_Date.append(word)
			check = 7
			print (word, "goes in Date \n")

		if word in Time:
			Stack_Time.append(word)
			check = 8
			print (word, "goes in Time \n")

		if word in DateTime:
			if DateTime[word]==1:
				Stack_Next.append(word)
				print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				print (word, "goes in Prev \n")

## if not empty then word in datetime(stack 3) is filled first in either of two stacks 
	elif len(Stack_Prev)!=0:

		temporary = Stack_Prev.pop()

		if check==7:
			Stack_Date.append(temporary)
			print (temporary, "goes in Date from Prev\n")

		elif check==8:
			Stack_Time.append(temporary)
			print (temporary, "goes in Time from Prev\n")

		if word in Date:
			Stack_Date.append(word)
			print (word, "goes in Date \n")
			check = 7

		if word in Time:
			Stack_Time.append(word)
			print (word, "goes in Time \n")
			check = 8

		if word in DateTime:

			Stack_Prev.append(temporary)

			if DateTime[word]==1:
				Stack_Next.append(word)
				print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				print (word, "goes in Prev \n")

	elif len(Stack_Next)!=0:

		#temp = []
		temp.append(Stack_Next.pop())

		#next_word = words[words.index(word)+1]

		if word in Date:
			Stack_Date.extend(temp)
			print (temp, "goes in Date from Next\n")
			temp.clear()
			Stack_Date.append(word)
			print (word, "goes in Date \n")
			check = 7
		
		elif word in Time:
			Stack_Time.extend(temp)
			print (temp, "goes in Time from Next\n")
			temp.clear()
			Stack_Time.append(word)
			print (word, "goes in Time \n")
			check = 8
		
		if word in DateTime:

			if DateTime[word]==1:
				Stack_Next.append(word)
				print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				print (word, "goes in Prev \n")

print (Stack_Date, " ")
print (Stack_Time, " ")
