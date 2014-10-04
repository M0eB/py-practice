# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex18 - Functions and Variables
# =============================================================================


def cheese_and_crackers( cheese_count, boxes_of_crackers ):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!\n" % boxes_of_crackers


print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers( amount_of_cheese, amount_of_crackers)


print "We can even do math inside:"
cheese_and_crackers( 10 + 20, 5 + 6 )


print "And we can combine the two, variables and math:"
cheese_and_crackers( amount_of_cheese + 100, amount_of_crackers + 1000 )


