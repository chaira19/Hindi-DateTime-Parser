import datetime 

## get the input
string = input("Give the text:")

## split the input into list
words = string.split(" ")

## give final date and time after parsing
def answer ( y=0,  mt=0, w=0,  d=0,  h=0,  m=0,  s=0):

	mt = mt + 12*y
	d = d + 30*mt

	now = datetime.datetime.now()
	change = datetime.timedelta( weeks =w, days=d, hours = h, minutes =m, seconds = s)
	print (now + change)

## Three category of words
Date = {"aaj":"0", "kal":"1", "parson":"2"}
Time = {"abhi":"0"}
DateTime = {"baad":"1", "pahle":"-1", "pichle":"-1", "agle":"1"}

## general class for getting stack object
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
       return len(self.items)
       
    def print(self):
    	return " ".join(items)

## three stacks
Stack_Date = Stack()
Stack_Time = Stack()
Stack_DateTime = Stack()

## Algorithm to fill all the words in stack
for word in words:

## if datetime(stack 3) is empty then fill accordingle
	if Stack_DateTime.isEmpty:

		if Date.has_key("word"):
			Stack_Date.append("word")

		if Time.has_key("word"):
			Stack_Time.append("word")

		if DateTime.has_key("word"):
			Stack_DateTime.append("word")

## if not empty then word in datetime(stack 3) is filled first in either of two stacks 
	else:

		temporary = Stack_DateTime.pop()

		if Date.has_key(temporary):
			Stack_Date.append(temporary)

		else:
			Stack_Time.append(temporary)

		if Date.has_key("word"):
			Stack_Date.append("word")

		if Time.has_key("word"):
			Stack_Time.append("word")

		if DateTime.has_key("word"):
			Stack_DateTime.append("word")
print(Stack_Time.print())