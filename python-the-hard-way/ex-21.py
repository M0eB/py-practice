# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex21 - Functions Can Return Something
# =============================================================================


def add( a, b ):
	print "ADDING %d + %d" % ( a, b )
	return a + b


def subtract( a, b ):
	print "SUBTRACTING %d - %d" % ( a, b )
	return a - b

def multiply( a, b ):
	print "MULTIPLYING %d * %d" % ( a, b )
	return a * b


def divide( a, b ):
	print "DIVIDING %d / %d" % ( a , b )
	return a / b	


print "Do some math :"

res1 = add( 30, 5 )
res2 = subtract( 80, 4 )
res3 = multiply( 90, 2 )
res4 = divide(200, 2)

print "Results:\n 1: %d\n 2: %d\n 3: %d\n 4: %d\n" % ( res1, res2, res3, res4 )


