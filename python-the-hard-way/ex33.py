# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex33 - While Loops
# =============================================================================


def while_loop(limit, step):
	i = 0
	numbers = []

	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)

		i += step
		print "Numbers now:", numbers
		print "At the buttom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num



def for_loop(limit, step):
	
	numbers = []

	for i in range(0, limit, step):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now:", numbers
		print "At the buttom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num



input = raw_input("Enter limit : ")
limit = int(input)

input = raw_input("Enter step size : ")
steps = int(input)

while_loop( limit, steps )
for_loop( limit, steps ) 