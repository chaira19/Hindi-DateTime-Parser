import stack
from stack import *

import parser
from parser import *

def HindiParser(string):

	## convert input to lower case
	string = string.lower()

	## split the input into words(list)
	words = string.split(" ")

	## get the dictinary of stacks
	Final = stack_algo(words)

	# empty function makes empty

	## Get parsed dictionary from Final Dictionary
	Answer = get_parsed(Final)

	return Answer

def GetEmails(string):

	string = string.lower()

	words = string.split(" ")

	emails = get_emails_parsed(words)

	return emails




