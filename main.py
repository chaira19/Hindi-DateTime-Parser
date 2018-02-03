import stack
from stack import *

import parser
from parser import *

import voice
from voice import *

## get the input
## input or raw_input
 
string=voice_input()

## convert inpurt to lower case
string = string.lower()

## split the input into words(list)
words = string.split(" ")

## get the dictinary of stacks
Final = stack_algo(words)

# empty function makes empty

## Get parsed dictionary from Final Dictionary
Answer =get_parsed(Final)
#Answer="DIP  DIP  POTATO CHIP"

#speaks out the string Answer
voice_output(Answer)

emails = get_emails_parsed(words)

if len(emails)!=0:

        print (emails)



