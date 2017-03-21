import data
from data import *

def stack_algo(words):

	## four stacks
	Stack_Date = []
	Stack_Time = []
	Stack_Next = []
	Stack_Prev = []

	temp = []
	check = 0

	## list of lists
	Stack_of_Stacks = []

	Stack_Index = []

	Final = {'Date':[], 'Time':[]}

	## Algorithm to fill all the words in stack
	for word in words:

		if word in Separators:

			#prev_word = words[words.index(word)-1]

			if check == 7:
				copy = Stack_Date[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Date, "Date Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Date.clear()
				Stack_Date = [x for x in Stack_Date if x]
				#print (Stack_Date, "Date Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Date")
				Final['Date'].append(copy)
				
			if check == 8:
				copy = Stack_Time[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Time, "Time Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Time.clear()
				Stack_Time = [x for x in Stack_Time if x]
				#print (Stack_Time, "Time Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Time")
				Final['Time'].append(copy)
				
			Stack_of_Stacks.append(word)
			#print(word, "goes in Full Stack \n")
			#print (Stack_of_Stacks, "\n")
			check = 0
			Stack_Index.append(word)
			
	## if next and prev stack is empty then fill accordingly
		if len(Stack_Next)==0 and len(Stack_Prev)==0:

			if (word in Date) or ((word.isdigit()) and (len(word)==4)):

				if(check == 8):
					copy = Stack_Time[:]
					Stack_of_Stacks.append(copy)
					#print (Stack_Time, "Time Stack goes in Full Stack \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Time.clear()
					Stack_Time = [x for x in Stack_Time if x]
					#print (Stack_Time, "Time Stack Cleared \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Index.append("Time")
					Final['Time'].append(copy)

				Stack_Date.append(word)
				check = 7
				#print (word, "goes in Date \n")

			if word in Time:

				if(check == 7):
					copy = Stack_Date[:]
					Stack_of_Stacks.append(copy)
					#print (Stack_Date, "Date Stack goes in Full Stack \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Date.clear()
					Stack_Date = [x for x in Stack_Date if x]
					#print (Stack_Date, "Date Stack Cleared \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Index.append("Date")
					Final['Date'].append(copy)

				Stack_Time.append(word)
				check = 8
				#print (word, "goes in Time \n")

			if word in DateTime:
				if DateTime[word][1]==1:
					Stack_Next.append(word)
					#print (word, "goes in Next \n")
				else :
					Stack_Prev.append(word)
					#print (word, "goes in Prev \n")

			elif word in Numbers:
				if Numbers[word][1]==1:
					Stack_Next.append(word)
					#print (word, "goes in Next \n")
				else :
					Stack_Prev.append(word)
					#print (word, "goes in Prev \n")

	## if not empty then word in datetime(stack 3) is filled first in either of two stacks 
		elif len(Stack_Prev)!=0:

			temporary = Stack_Prev.pop()

			if check==7:
				Stack_Date.append(temporary)
				#print (temporary, "goes in Date from Prev\n")

			elif check==8:
				Stack_Time.append(temporary)
				#print (temporary, "goes in Time from Prev\n")

			if (word in Date) or ((word.isdigit()) and (len(word)==4)):

				if(check == 8):
					copy = Stack_Time[:]
					Stack_of_Stacks.append(copy)
					#print (Stack_Time, "Time Stack goes in Full Stack \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Time.clear()
					Stack_Time = [x for x in Stack_Time if x]
					#print (Stack_Time, "Time Stack Cleared \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Index.append("Time")
					Final['Time'].append(copy)
			
				Stack_Date.append(word)
				#print (word, "goes in Date \n")
				check = 7

			if word in Time:

				if(check == 7):
					copy = Stack_Date[:]
					Stack_of_Stacks.append(copy)
					#print (Stack_Date, "Date Stack goes in Full Stack \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Date.clear()
					Stack_Date = [x for x in Stack_Date if x]
					#print (Stack_Date, "Date Stack Cleared \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Index.append("Date")
					Final['Date'].append(copy)

				Stack_Time.append(word)
				#print (word, "goes in Time \n")
				check = 8

			if word in DateTime:

				Stack_Prev.append(temporary)

				if DateTime[word][1]==1:
					Stack_Next.append(word)
					#print (word, "goes in Next \n")
				else :
					Stack_Prev.append(word)
					#print (word, "goes in Prev \n")

			elif word in Numbers:

				Stack_Prev.append(temporary)

				if Numbers[word][1]==1:
					Stack_Next.append(word)
					#print (word, "goes in Next \n")
				else :
					Stack_Prev.append(word)
					#print (word, "goes in Prev \n")

		elif len(Stack_Next)!=0:

			#temp = []
			temp.append(Stack_Next.pop())

			#next_word = words[words.index(word)+1]

			if (word in Date) or ((word.isdigit()) and (len(word)==4)):
				Stack_Date.extend(temp)
				#print (temp, "goes in Date from Next\n")
				temp.clear()

				if(check == 8):
					copy = Stack_Time[:]
					Stack_of_Stacks.append(copy)
					#print (Stack_Time, "Time Stack goes in Full Stack \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Time.clear()
					Stack_Time = [x for x in Stack_Time if x]
					#print (Stack_Time, "Time Stack Cleared \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Index.append("Time")
					Final['Time'].append(copy)

				Stack_Date.append(word)
				#print (Stack_Date)
				#print (word, "goes in Date \n")
				check = 7
			
			elif word in Time:
				Stack_Time.extend(temp)
				#print (temp, "goes in Time from Next\n")
				temp.clear()

				if(check == 7):
					copy = Stack_Date[:]
					Stack_of_Stacks.append(copy)
					#print (Stack_Date, "Date Stack goes in Full Stack \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Date.clear()
					Stack_Date = [x for x in Stack_Date if x]
					#print (Stack_Date, "Date Stack Cleared \n")
					#print (Stack_of_Stacks, "\n")
					Stack_Index.append("Date")
					Final['Date'].append(copy)

				Stack_Time.append(word)
				#print (word, "goes in Time \n")
				check = 8
			
			if word in DateTime:

				if DateTime[word][1]==1:
					Stack_Next.append(word)
					#print (word, "goes in Next \n")
				else :
					Stack_Prev.append(word)
					#print (word, "goes in Prev \n")

			elif word in Numbers:
				if Numbers[word][1]==1:
					Stack_Next.append(word)
					#print (word, "goes in Next \n")
				else :
					Stack_Prev.append(word)
					#print (word, "goes in Prev \n")

		if words.index(word) == len(words)-1:

			if len(Stack_Prev)!=0:

				temporary = Stack_Prev.pop()

				if check==7:
					Stack_Date.append(temporary)
					#print (temporary, "goes in Date from Prev\n")

				elif check==8:
					Stack_Time.append(temporary)
					#print (temporary, "goes in Time from Prev\n")

			if len(Stack_Next)!=0:

				temporary = Stack_Next.pop()

				if check==7:
					Stack_Date.append(temporary)
					#print (temporary, "goes in Date from Next\n")

				elif check==8:
					Stack_Time.append(temporary)
					#print (temporary, "goes in Time from Next\n")	

			if len(Stack_Date)!=0:
				copy = Stack_Date[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Date, "Last Stack(Date) goes in Full Stack")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Date")
				Final['Date'].append(copy)

			elif len(Stack_Time)!=0:
				copy = Stack_Time[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Time, "Last Stack(Time) goes in Full Stack")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Time")
				Final['Time'].append(copy)

	print (Stack_of_Stacks, "\n")
	print (Stack_Index, "\n")
	print (Final)

	return Final
