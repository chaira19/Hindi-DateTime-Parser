import voice
from voice import *

import stack
from stack import *

import parser
from parser import *

## get the input
## input or raw_input
#string = input("Give the text:")
string = voice_input()

## convert inpurt to lower case
string = string.lower()

## split the input into words(list)
words = string.split(" ")

## get the dictinary of stacks
Final = stack_algo(words)

# empty function makes empty

## Get parsed dictionary from Final Dictionary
Answer = parser.get_parsed(Final)

print (Answer)

emails = get_emails(words)

if len(emails)!=0:

	print (emails)




