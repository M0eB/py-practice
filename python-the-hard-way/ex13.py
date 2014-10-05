# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex13 - Parameters, Unpacking, Variables
# =============================================================================


# argv ------------------------------------------------------------------------
#
# Create a script that requires 3 additional command-line arguments as input
# If the script is run without the required arguments, the following error
# will appear : 
#		ValueError: need more than 1 value to unpack
# Unpacking refers to assigning the inputs in the argument vector to variables
#
# -----------------------------------------------------------------------------


from sys import argv

script, first, second, third = argv       # store input arguments

print "The script is called:", script     # first argument is always the script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


