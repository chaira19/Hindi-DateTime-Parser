import data
from data import *

import functions
from functions import *

def get_parsed(Final={}):


	Answer = {'Date':[], 'Time':[]}

	for date in Final['Date']:

		fulldate = []
		y=0
		mt=0
		w=0
		d=0

		x = set(date).intersection(DateTime.keys())
		yx = set(date).intersection(Numbers.keys())

		if len(x)>0:

			if len(yx)>0:
				
				if ('din' in date) or ('divas' in date) or ('dino' in date):
					d = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

				#why not if ('ghanta' or 'ghante') in time:
				if ('mahine' in date) or ('mahina' in date):
					mt = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

				if ('saal' in date) or ('varsh' in date):
					y = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

				if ('hafta' in date) or ('hafte' in date):
					w = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

			else:
				## eleiminate this step by use of above step (putting value = 1)

				if ('din' in date) or ('divas' in date) or ('dino' in date):
					d = DateTime[list(x)[0]][0]

				#why not if ('ghanta' or 'ghante') in time:
				if ('mahine' in date) or ('mahina' in date):
					mt = DateTime[list(x)[0]][0]

				if ('saal' in date) or ('varsh' in date):
					y = DateTime[list(x)[0]][0]

				if ('hafta' in date) or ('hafte' in date):
					w = DateTime[list(x)[0]][0]

				### Instead of using [0] use previous word for (aaj agle mahine pichle saal)

		#	for word in date:

				#if Date[word][1] == 'weekday':

				#	prev_word = date[date.index(word)-1]

				#	if prev_word == 'agle':

				#		print ("")

				#	elif prev_word == 'pichle':

				#		print ("")

				#	elif prev_word == 'is':

				#		print ("")

			## pass in format of WE(+1) where WE is not string

			Answer['Date'].append(change_datetime("date",y,mt,w,d))


		else:
			
			if len(set(date).intersection(Numbers.keys()))>0:
				
				for word in date:

					if word in Numbers.keys():

						next_word = date[date.index(word)+1]

						if (next_word == 'mahina') or (next_word == 'mahine'): ## check if next_word == 'mahina' or 'mahine' works or not
							mt = Numbers[word][0]

						elif (next_word == 'saal') or (next_word == 'varsh'):
							y = Numbers[word][0]

						elif (next_word == 'tarikh') or (next_word == 'din'):
							d = Numbers[word][0]

						elif (next_word.isdigit()) and (len(next_word)==4):
							mt = Numbers[word][0]

						elif Date[next_word][1] == 'month':
							d = Numbers[word][0]
				
				#fulldate.append(set_datetime(y,mt,d))

				## Do something like if month in date then d=number , mt = month[0]

			for word in date:

				if (word in Date) and (Date[word][1] == 'month'):
					mt = Date[word][0]
					next_word = date[date.index(word)+1]

					if next_word in Numbers:
						d = Numbers[next_word][0]
				#obviously word is in Date

				if (word.isdigit()) and (len(word)==4):
					y = int(word)

				if len(date) == date.index(word)+1:
					fulldate.append(set_datetime(y, mt, d))

				if word == 'aaj':
					fulldate.append(change_datetime("date",0,0,0,0))

				if word == 'kal':
					fulldate.append(change_datetime("date",0,0,0,1))

				if word == 'parson':
					fulldate.append(change_datetime("date",0,0,0,2))

				if word == 'narson':
					fulldate.append(change_datetime("date",0,0,0,3))

				## Above 4 can be transformed into 1 just like done in above 4

				#if (word in Date) and (Date[word][1] == 'weekday'):
				# Difficult to implement without  DateTime words i.e. to set the day according to month and year
				## pseudocode
				## if (word in Date) and (Date[word][1] == 'weekday'):
					#if (y!=0) and (mt!=0):

						#print ("")
				##          call weekday function passing month and year to get the date	

			Answer['Date'].append(fulldate)

			

	for time in Final['Time']:

		h=0
		m=0
		s=0
		c=0

		x = set(time).intersection(DateTime.keys())
		y = set(time).intersection(Numbers.keys())

		if len(y) == 0:
			y.add("1")

		#print (x)
		#print (y)

		if len(x)>0:

			if len(y)>0:

				if ('ghanta' in time) or ('ghante' in time) or ('ghanton' in time):
					h = Numbers[list(y)[0]][0] * DateTime[list(x)[0]][0]

				#why not if ('ghanta' or 'ghante') in time:
				if ('minute' in time) or ('minutes' in time):
					m = Numbers[list(y)[0]][0] * DateTime[list(x)[0]][0]

				if ('second' in time) or ('seconds' in time):
					s = Numbers[list(y)[0]][0] * DateTime[list(x)[0]][0]

			else:

				print ("waited for this example, thanks !!")

				# if pichle (ghante then , minute then, second then) else agle (same)

			Answer['Time'].append(change_datetime("time",0,0,0,0,h,m,s))

		else:

			if len(set(time).intersection(Numbers.keys()))>0:

				#print ("Number Exist")

				for word in time:

					if word in Numbers.keys():

						next_word = time[time.index(word)+1]

						if (next_word == 'baj') or (next_word == 'baje'): ## baje is not working
							h = Numbers[word][0]
							print (h, "h")

						elif (next_word == 'minute') or (next_word == 'minutes') or (next_word == 'min'): ## or ke baad wale main dikkar hai
							m = Numbers[word][0]
							print (m, "m")

						elif (next_word == 'second') or (next_word == 'seconds') or (next_word == 'sec'):
							s = Numbers[word][0]
							print (s, "s")

				if 'subah' in time:
					c = "AM"

				elif 'dopahar' in time:
					c = "PM"

				elif 'shaam' or 'sandhya' in time: ## sandhya to aa hi nahi raha
					c = "PM"

				elif ('raat' in time) and (0 <= h < 6):
					c = "AM"

				elif ('raat' in time) and (6 <= h < 12):
					c = "PM"

				print (c, "c")
				Answer['Time'].append(set_datetime(0,0,0,h,m,s,c))

			else:

				#print ("Number doesn't Exist")

				duration = []
				
				for word in time:

					if word == 'abhi':
						duration.append(change_datetime("time"))

					if word == 'subah':
						duration.append("5 - 12 AM")

					elif word == 'dopahar':
						duration.append("12 - 5 PM")

					elif word == ('shaam' or 'sandhya'):
						duration.append("5 - 12 PM")

					elif word == 'raat':
						duration.append("10-12 PM & 12 - 5 AM")

				Answer['Time'].append(duration)

	return Answer

def get_emails_parsed(words):

	emails = []

	for word in words:

		if ('.' in word) and ('@' in word):

			emails.append(word)

	return emails 