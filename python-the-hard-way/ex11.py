# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex11-12 - Asking Questions
# =============================================================================

# USER INPUT ------------------------------------------------------------------
#
# 		my_var = raw_input() 
# 		my_var = raw_input( " What is Your Name ? ")
# 		my_int = int( raW_input() )
#
# -----------------------------------------------------------------------------


# Get some user input ---------------------------------------------------------

print "How tall are you ?"
height = raw_input()

print "How much do you weigh ?"
weight = raw_input()

print "So, you're %s tall, and %s heavy." % (height, weight)


# Let's Do this a little more efficiently -------------------------------------

height = raw_input( "How tall are you ?" )
weight = raw_input( "How much do you weigh?" )

print "So, you're %r tall, and %r heavy." % (height, weight)


# Let's get some integers -----------------------------------------------------

print "Give me a number : "
my_int = int( raw_input() )

print "Your input doubled is : %d" % (my_int * 2)


