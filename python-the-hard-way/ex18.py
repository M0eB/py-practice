# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex18 - Names, Variables, Code, Functions		
# =============================================================================


# This one is like your scripts with argv
def print_two( *args ):
	arg1, arg2 = args  #unpack arguments
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args i actually pointless, we can do this
def print_two_again( arg1, arg2 ):
	print "arg1: %r, arg2: %r" % (arg1, arg2)


# This just takes one argument
def print_one( arg1 ):
	print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
	print "I got nothin'."


print_two( "Mohamed", "Ismail" )
print_two_again( "Mohamed", "Ismail" )
print_one( "First!" )
print_none()


