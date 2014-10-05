# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex25 - Even More Practice
# =============================================================================


# Importing -------------------------------------------------------------------
# 
#  Basic import : import ex25
#                 Call functions using ex25.break_words( "test sentence" )
#
# Avoid "ex25." : from ex25 import *
#                 Call functions directly - break_words( "sentence" )
#
# -----------------------------------------------------------------------------


# Help Files ------------------------------------------------------------------
#
# 	- Document functions using """comments""" after the function definition
#	- You can view the descriptions by calling help(module) ex- "help(ex25)"
#	- Any comments at the start of the file are also displayed 
#
# -----------------------------------------------------------------------------


def break_words( stuff ):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words( words ):
	"""Sort the words"""
	return sorted(words)

def print_first_word( words ):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word( words ):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence( sentence ):
	"""Takes in a full snetence and returns the sorted words."""
	words = break_words( sentence )
	return sort_words( words ) 

def print_first_and_last( sentence ):
	"""Prints the first and last words of the sentence."""
	words = break_words( sentence )
	print_first_word( words )
	print_last_word( words )

def print_first_and_last_sorted( sentence ):
	"""Sorts the words then prints teh first and last."""
	words = sort_sentence( sentence )
	print_first_word( words )
	print_last_word( words )


