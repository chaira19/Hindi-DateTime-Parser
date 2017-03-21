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



