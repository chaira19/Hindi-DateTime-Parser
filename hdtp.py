#!/usr/bin/python3

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

def GetIndianPhoneNumbers(string):

	words = string.split(" ")

	phonenumbers = get_numbers_parsed(words)

	return phonenumbers

def DiseaseFinder(ln, string): 

	## use language detection
	## or convert without depending on input language

	if (ln == "en") or (ln == "english"):

		disease_name = get_disease(string)
		return disease_name

	if (ln == "hi") or (ln == "hindi"):

		##first translate string
		disease_name = get_disease(string)
		return disease_name


def GetSentences(str):

	return get_sentences(str)

def GetTokens(str):

	return get_tokens(str)

## if input text is nul for every function, ask for the text





